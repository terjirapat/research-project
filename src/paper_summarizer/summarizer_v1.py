from typing import Dict
from src.prompt.paper_summarizer import PromptPaperSummarizer
from src.llms.base import BaseLLM
from src.utils.loader import load_json
from src.utils.logger import log_execution_time

SECTION_PROMPT_MAP = {
    "abstract": PromptPaperSummarizer.abstract,
    "introduction": PromptPaperSummarizer.introduction,
    "related_work": PromptPaperSummarizer.related_work,
    "methodology": PromptPaperSummarizer.methodology,
    "result": PromptPaperSummarizer.result,
    "discussion": PromptPaperSummarizer.discussion,
    "conclusion": PromptPaperSummarizer.conclusion,
}

SECTION_DISPLAY_NAMES = {
    "abstract": "Abstract",
    "introduction": "Introduction",
    "related_work": "Related Work",
    "methodology": "Methodology",
    "result": "Results",
    "discussion": "Discussion",
    "conclusion": "Conclusion",
}


def dict_to_text(d: dict) -> str:
    sections = []
    for k, v in d.items():
        sections.append(f"### {k}\n{v}")
    return "\n\n".join(sections)


def summarize_section(llm: BaseLLM, section_content: dict | str, system_prompt: str) -> str:
    if isinstance(section_content, dict):
        text = dict_to_text(section_content)
    else:
        text = section_content

    if not text.strip():
        return ""

    messages = [{"role": "user", "content": text}]
    response = llm.run(system_prompt, messages)
    return response.content

@log_execution_time
def summarize_all_sections(llm: BaseLLM, paper: dict) -> Dict[str, str]:
    summaries = {}
    for section_key, prompt_fn in SECTION_PROMPT_MAP.items():
        content = paper.get(section_key)
        if not content:
            continue
        summary = summarize_section(llm, content, prompt_fn())
        if summary:
            summaries[section_key] = summary
    return summaries

@log_execution_time
def export_summaries_to_md(summaries: Dict[str, str], output_path: str, title: str = "Paper Summary") -> None:
    lines = [f"# {title}\n"]
    for section_key, summary in summaries.items():
        display_name = SECTION_DISPLAY_NAMES.get(section_key, section_key)
        lines.append(f"## {display_name}\n")
        lines.append(f"{summary}\n")

    from pathlib import Path
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    Path(output_path).write_text("\n".join(lines), encoding="utf-8")

@log_execution_time
def run_summarize_pipeline(
    llm: BaseLLM,
    paper_json_path: str,
    output_md_path: str,
    title: str = "Paper Summary",
) -> Dict[str, str]:
    paper = load_json(paper_json_path)
    summaries = summarize_all_sections(llm, paper)
    export_summaries_to_md(summaries, output_md_path, title)
    return summaries
