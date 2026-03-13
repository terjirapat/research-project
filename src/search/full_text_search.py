import math
import re
from collections import defaultdict
from typing import Dict, List, Tuple

from src.utils.logger import log_execution_time


class InvertedIndex:
    """
    Simple full-text search engine using an inverted index with TF-IDF scoring.
    """

    def __init__(self) -> None:
        self._documents: Dict[str, str] = {}
        self._index: Dict[str, Dict[str, int]] = defaultdict(dict)
        self._doc_count: int = 0

    def add_documents(self, documents: Dict[str, str]) -> None:
        """
        Add multiple documents and build the inverted index.
        """
        self._documents.update(documents)
        self._doc_count = len(self._documents)
        self._build_index()

    @log_execution_time
    def search(self, query: str, top_k: int = 5) -> List[Tuple[str, float]]:
        """
        Search documents using AND logic with TF-IDF ranking.
        Returns list of (doc_id, score).
        """
        tokens = self._tokenize(query)
        candidate_docs = self._get_candidate_documents(tokens)

        scores = {
            doc_id: self._compute_score(doc_id, tokens)
            for doc_id in candidate_docs
        }

        ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        return ranked[:top_k]

    def _build_index(self) -> None:
        """
        Build inverted index: term -> {doc_id: term_frequency}
        """
        self._index.clear()

        for doc_id, text in self._documents.items():
            tokens = self._tokenize(text)
            term_freq = self._term_frequency(tokens)

            for term, freq in term_freq.items():
                self._index[term][doc_id] = freq

    @staticmethod
    def _tokenize(text: str) -> List[str]:
        """
        Lowercase + simple word split.
        """
        text = text.lower()
        return re.findall(r"\b\w+\b", text)

    @staticmethod
    def _term_frequency(tokens: List[str]) -> Dict[str, int]:
        """
        Count frequency of each token in a document.
        """
        freq = defaultdict(int)
        for token in tokens:
            freq[token] += 1
        return freq

    def _get_candidate_documents(self, tokens: List[str]) -> List[str]:
        """
        Get documents that contain ALL query terms.
        """
        if not tokens:
            return []

        doc_sets = [
            set(self._index[token].keys())
            for token in tokens
            if token in self._index
        ]

        if not doc_sets:
            return []

        return list(set.intersection(*doc_sets))

    def _compute_score(self, doc_id: str, tokens: List[str]) -> float:
        """
        Compute TF-IDF score for a document.
        """
        score = 0.0

        for token in tokens:
            if token not in self._index:
                continue

            tf = self._index[token].get(doc_id, 0)
            df = len(self._index[token])

            if df == 0:
                continue

            idf = math.log((1 + self._doc_count) / (1 + df)) + 1
            score += tf * idf

        return score