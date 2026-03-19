from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Dict

from src.llms.base import BaseLLM, UserMessage
from src.prompt.paper_summarizer import PromptPaperSummarizer
from src.utils.loader import load_json
from src.utils.logger import log_execution_time


# =========================
# Config Layer
# =========================

@dataclass(frozen=True)
class Section:
    key: str
    display: str
    prompt: Callable[[], str]


SECTIONS = [
    Section("abstract", "Abstract", PromptPaperSummarizer.abstract),
    Section("introduction", "Introduction", PromptPaperSummarizer.introduction),
    Section("related_work", "Related Work", PromptPaperSummarizer.related_work),
    Section("methodology", "Methodology", PromptPaperSummarizer.methodology),
    Section("result", "Results", PromptPaperSummarizer.result),
    Section("discussion", "Discussion", PromptPaperSummarizer.discussion),
    Section("conclusion", "Conclusion", PromptPaperSummarizer.conclusion),
]


# =========================
# LLM Layer
# =========================

def call_llm(llm: BaseLLM, system_prompt: str, text: str) -> str:
    if not text.strip():
        return ""
    response = llm.run(system_prompt, [UserMessage(text)])
    return response.content


# =========================
# Transform Layer
# =========================

def dict_to_markdown(data: Dict[str, str]) -> str:
    return "\n\n".join(f"### {k}\n{v}" for k, v in data.items())


def normalize_content(content: dict | str) -> str:
    if isinstance(content, dict):
        return dict_to_markdown(content)
    return content


# =========================
# Core Logic
# =========================

def summarize_section(
    llm: BaseLLM,
    content: dict | str,
    prompt: str,
) -> str:
    text = normalize_content(content)
    return call_llm(llm, prompt, text)


@log_execution_time
def summarize_sections(llm: BaseLLM, paper: dict) -> Dict[str, str]:
    results = {}

    for section in SECTIONS:
        content = paper.get(section.key)
        if not content:
            continue

        summary = summarize_section(
            llm,
            content,
            section.prompt(),
        )

        if summary:
            results[section.key] = summary

    return results


@log_execution_time
def summarize_global(llm: BaseLLM, summaries: Dict[str, str]) -> str:
    text = dict_to_markdown(summaries)
    return call_llm(llm, PromptPaperSummarizer.global_summary(), text)


# =========================
# IO Layer
# =========================

def ensure_output_dir(path: str | Path) -> Path:
    path = Path(path).resolve()
    path.mkdir(parents=True, exist_ok=True)
    return path


def write_markdown(path: Path, title: str, heading: str, body: str) -> None:
    content = f"# {title} — {heading}\n\n{body}\n"
    path.write_text(content, encoding="utf-8")


def export_markdown(
    summaries: Dict[str, str],
    output_dir: str | Path,
    title: str,
    global_summary: str,
) -> None:
    out = ensure_output_dir(output_dir)

    section_map = {s.key: s.display for s in SECTIONS}

    for key, summary in summaries.items():
        heading = section_map.get(key, key)
        write_markdown(out / f"{key}.md", title, heading, summary)

    if global_summary:
        write_markdown(out / "global_summary.md", title, "Global Summary", global_summary)


# =========================
# Pipeline
# =========================

@log_execution_time
def run_summarize_pipeline(
    llm: BaseLLM,
    paper_path: str | Path,
    output_dir: str | Path,
    title: str = "Paper Summary",
) -> Dict[str, str]:

    paper = load_json(paper_path)

    section_summaries = summarize_sections(llm, paper)

    global_summary = summarize_global(llm, section_summaries)

    export_markdown(
        summaries=section_summaries,
        output_dir=output_dir,
        title=title,
        global_summary=global_summary,
    )

    return {
        **section_summaries,
        "global_summary": global_summary,
    }