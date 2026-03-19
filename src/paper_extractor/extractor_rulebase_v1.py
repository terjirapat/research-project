import re
from pathlib import Path
from typing import Dict, List
from src.utils.logger import log_execution_time
from docling.document_converter import DocumentConverter


converter = DocumentConverter()


def convert_paper_to_markdown(path: str | Path, converter: DocumentConverter) -> str:
    """Convert document to markdown."""
    doc = converter.convert(str(path)).document
    return doc.export_to_markdown()


def split_markdown_sections(markdown: str) -> Dict[str, str]:
    """Split markdown into sections using heading titles."""
    
    sections: Dict[str, str] = {}
    current_title: str | None = None
    buffer: List[str] = []

    for line in markdown.splitlines():

        header_match = re.match(r"^#{1,6}\s+(.*)", line)

        if header_match:

            if current_title:
                sections[current_title] = "\n".join(buffer).strip()

            current_title = header_match.group(1).strip()
            buffer = []
            continue

        buffer.append(line)

    if current_title:
        sections[current_title] = "\n".join(buffer).strip()

    return sections


def map_sections_to_schema(
    sections: Dict[str, str],
    section_aliases: Dict[str, List[str]],
) -> Dict[str, str]:
    """Map parsed sections to normalized research paper schema."""

    paper: Dict[str, str] = {key: "" for key in section_aliases}

    for title, content in sections.items():

        title_lower = title.lower()

        for section_key, aliases in section_aliases.items():

            if any(alias in title_lower for alias in aliases):
                paper[section_key] += content

    return paper

@log_execution_time
def extract_paper_sections(
    path: str | Path,
    section_aliases: Dict[str, List[str]],
    converter: DocumentConverter = converter,
) -> Dict[str, str]:
    """Full pipeline: document -> markdown -> parsed sections -> mapped schema"""

    markdown = convert_paper_to_markdown(path, converter)

    sections = split_markdown_sections(markdown)

    paper = map_sections_to_schema(sections, section_aliases)

    return paper