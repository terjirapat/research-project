from pathlib import Path

class PromptPaperSummarizer:
    base_dir = Path(__file__).parent

    @staticmethod
    def abstract():
        return (PromptPaperSummarizer.base_dir / "abstract.md").read_text(encoding='utf-8')
    
    @staticmethod
    def conclusion():
        return (PromptPaperSummarizer.base_dir / "conclusion.md").read_text(encoding='utf-8')

    @staticmethod
    def discussion():
        return (PromptPaperSummarizer.base_dir / "discussion.md").read_text(encoding='utf-8')

    @staticmethod
    def introduction():
        return (PromptPaperSummarizer.base_dir / "introduction.md").read_text(encoding='utf-8')
    
    @staticmethod
    def method():
        return (PromptPaperSummarizer.base_dir / "method.md").read_text(encoding='utf-8')
    
    @staticmethod
    def related_work():
        return (PromptPaperSummarizer.base_dir / "related_work.md").read_text(encoding='utf-8')
    
    @staticmethod
    def result():
        return (PromptPaperSummarizer.base_dir / "result.md").read_text(encoding='utf-8')