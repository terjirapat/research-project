import math
import re
import numpy as np
from collections import defaultdict
from typing import Callable, Dict, List, Tuple

from src.utils.logger import log_execution_time


class HybridSearchEngine:
    """
    Hybrid search engine combining keyword TF-IDF and vector cosine similarity.
    """

    def __init__(
        self,
        embedding_fn: Callable[[str], np.ndarray],
        alpha: float = 0.5,
        beta: float = 0.5,
    ) -> None:
        self._embedding_fn = embedding_fn
        self._alpha = alpha
        self._beta = beta

        self._documents: Dict[str, str] = {}
        self._inverted_index: Dict[str, Dict[str, int]] = defaultdict(dict)
        self._doc_count: int = 0

        self._vectors: Dict[str, np.ndarray] = {}
        self._normalized_vectors: Dict[str, np.ndarray] = {}

    # ---------- Public API ----------

    def add_documents(self, documents: Dict[str, str]) -> None:
        self._documents.update(documents)
        self._doc_count = len(self._documents)

        self._build_keyword_index()
        self._build_vector_index()

    @log_execution_time
    def search(self, query: str, top_k: int = 5) -> List[Tuple[str, float]]:
        keyword_scores = self._keyword_search(query)
        vector_scores = self._vector_search(query)

        combined_scores = self._combine_scores(keyword_scores, vector_scores)

        ranked = sorted(combined_scores.items(), key=lambda x: x[1], reverse=True)
        return ranked[:top_k]

    # ---------- Keyword Logic ----------

    def _build_keyword_index(self) -> None:
        self._inverted_index.clear()

        for doc_id, text in self._documents.items():
            tokens = self._tokenize(text)
            term_freq = self._term_frequency(tokens)

            for term, freq in term_freq.items():
                self._inverted_index[term][doc_id] = freq

    def _keyword_search(self, query: str) -> Dict[str, float]:
        tokens = self._tokenize(query)
        scores = defaultdict(float)

        for token in tokens:
            if token not in self._inverted_index:
                continue

            df = len(self._inverted_index[token])
            idf = math.log((1 + self._doc_count) / (1 + df)) + 1

            for doc_id, tf in self._inverted_index[token].items():
                scores[doc_id] += tf * idf

        return self._normalize_scores(scores)

    # ---------- Vector Logic ----------

    def _build_vector_index(self) -> None:
        for doc_id, text in self._documents.items():
            vector = self._embedding_fn(text)
            norm_vector = self._normalize_vector(vector)

            self._vectors[doc_id] = vector
            self._normalized_vectors[doc_id] = norm_vector

    def _vector_search(self, query: str) -> Dict[str, float]:
        query_vector = self._embedding_fn(query)
        query_norm = self._normalize_vector(query_vector)

        scores = {
            doc_id: float(np.dot(query_norm, doc_vector))
            for doc_id, doc_vector in self._normalized_vectors.items()
        }

        return self._normalize_scores(scores)

    # ---------- Fusion Logic ----------

    def _combine_scores(
        self,
        keyword_scores: Dict[str, float],
        vector_scores: Dict[str, float],
    ) -> Dict[str, float]:

        all_doc_ids = set(keyword_scores) | set(vector_scores)
        combined = {}

        for doc_id in all_doc_ids:
            k_score = keyword_scores.get(doc_id, 0.0)
            v_score = vector_scores.get(doc_id, 0.0)

            combined[doc_id] = self._alpha * k_score + self._beta * v_score

        return combined

    # ---------- Utilities ----------

    @staticmethod
    def _tokenize(text: str) -> List[str]:
        text = text.lower()
        return re.findall(r"\b\w+\b", text)

    @staticmethod
    def _term_frequency(tokens: List[str]) -> Dict[str, int]:
        freq = defaultdict(int)
        for token in tokens:
            freq[token] += 1
        return freq

    @staticmethod
    def _normalize_vector(vector: np.ndarray) -> np.ndarray:
        norm = np.linalg.norm(vector)
        return vector if norm == 0 else vector / norm

    @staticmethod
    def _normalize_scores(scores: Dict[str, float]) -> Dict[str, float]:
        if not scores:
            return {}

        max_score = max(scores.values())
        if max_score == 0:
            return scores

        return {k: v / max_score for k, v in scores.items()}