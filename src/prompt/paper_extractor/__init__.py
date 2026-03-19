from pathlib import Path

class PromptPaperExtractor:
    base_dir = Path(__file__).parent

    @staticmethod
    def section_grouper():
        return (PromptPaperExtractor.base_dir / "section_grouper.md").read_text(encoding='utf-8')