import json
import re
from pathlib import Path
from typing import Dict, List, Optional

from docling.document_converter import DocumentConverter

from src.llms.bedrock import BedrockNova
from src.llms.base import BaseLLM

from src.prompt.paper_extractor import PromptPaperExtractor

from src.utils.logger import log_execution_time, logger
from src.utils.loader import load_config

config_path = '../src/config/paper_extractor.yaml'
config = load_config(config_path)

TARGET_SECTIONS = config['target_sections']
llm = BedrockNova(model_id=config['llm_model'])

# ==========================================================
# Core Pipeline
# ==========================================================

@log_execution_time
def extract_paper_sections(
    path: str | Path,
    converter: Optional[DocumentConverter] = None,
) -> Dict[str, Dict[str, str]]:
    converter = converter or DocumentConverter()

    markdown = _convert_to_markdown(path, converter)
    raw_sections = _split_markdown(markdown)

    labels = _classify_sections_with_llm(raw_sections)

    return _group_sections_by_label(labels, raw_sections)


# ==========================================================
# Step 1: Convert document
# ==========================================================

def _convert_to_markdown(path: str | Path, converter: DocumentConverter) -> str:
    document = converter.convert(str(path)).document
    return document.export_to_markdown()


# ==========================================================
# Step 2: Split markdown into sections
# ==========================================================

def _split_markdown(markdown: str) -> Dict[str, str]:
    sections: Dict[str, str] = {}
    current_title: Optional[str] = None
    buffer: List[str] = []

    for line in markdown.splitlines():
        header = _extract_header(line)

        if header:
            if current_title:
                sections[current_title] = _join_buffer(buffer)

            current_title = header
            buffer = []
        else:
            buffer.append(line)

    if current_title:
        sections[current_title] = _join_buffer(buffer)

    return sections


def _extract_header(line: str) -> Optional[str]:
    match = re.match(r"^#{1,6}\s+(.*)", line)
    return match.group(1).strip() if match else None


def _join_buffer(buffer: List[str]) -> str:
    return "\n".join(buffer).strip()


# ==========================================================
# Step 3: LLM classification
# ==========================================================

def _classify_sections_with_llm(sections: Dict[str, str], llm: BaseLLM = llm) -> Dict[str, str]:
    section_titles = list(sections.keys())

    response = llm.run(
        PromptPaperExtractor.section_grouper(),
        [{"role": "user", "content": str(section_titles)}],
    )

    logger.info(
        "LLM tokens: input=%d output=%d",
        response.input_tokens,
        response.output_tokens,
    )

    return _parse_llm_json(response.content)


# ==========================================================
# Step 4: Parse LLM output
# ==========================================================

def _parse_llm_json(text: str) -> Dict[str, str]:
    cleaned = _remove_code_blocks(text)
    json_str = _extract_json_block(cleaned)
    json_str = _fix_trailing_commas(json_str)

    return json.loads(json_str)


def _remove_code_blocks(text: str) -> str:
    return re.sub(r"```.*?\n|```", "", text).strip()


def _extract_json_block(text: str) -> str:
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if not match:
        raise ValueError("No JSON found in LLM response")
    return match.group()


def _fix_trailing_commas(text: str) -> str:
    return re.sub(r",\s*}", "}", text)


# ==========================================================
# Step 5: Group sections
# ==========================================================

def _group_sections_by_label(
    labels: Dict[str, str],
    sections: Dict[str, str],
) -> Dict[str, Dict[str, str]]:
    grouped = {section: {} for section in TARGET_SECTIONS}

    for title, label in labels.items():
        if label in grouped and title in sections:
            grouped[label][title] = sections[title]

    return grouped