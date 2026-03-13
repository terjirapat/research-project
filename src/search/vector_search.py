import numpy as np
from typing import Callable, Dict, List, Tuple

from src.utils.logger import log_execution_time


class VectorSearchEngine:
    """
    Simple in-memory vector search using cosine similarity.
    """

    def __init__(self, embedding_fn: Callable[[str], np.ndarray]) -> None:
        """
        embedding_fn: function that converts text -> embedding vector
        """
        self._embedding_fn = embedding_fn
        self._vectors: Dict[str, np.ndarray] = {}
        self._normalized: Dict[str, np.ndarray] = {}

    def add_documents(self, documents: Dict[str, str]) -> None:
        """
        Convert documents to embeddings and store normalized vectors.
        """
        for doc_id, text in documents.items():
            vector = self._embedding_fn(text)
            norm_vector = self._normalize(vector)

            self._vectors[doc_id] = vector
            self._normalized[doc_id] = norm_vector

    @log_execution_time
    def search(self, query: str, top_k: int = 5) -> List[Tuple[str, float]]:
        """
        Return top_k most similar documents to query.
        """
        query_vector = self._embedding_fn(query)
        query_norm = self._normalize(query_vector)

        scores = {
            doc_id: self._cosine_similarity(query_norm, doc_vector)
            for doc_id, doc_vector in self._normalized.items()
        }

        ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        return ranked[:top_k]

    @staticmethod
    def _normalize(vector: np.ndarray) -> np.ndarray:
        """
        Normalize vector to unit length.
        """
        norm = np.linalg.norm(vector)
        if norm == 0:
            return vector
        return vector / norm

    @staticmethod
    def _cosine_similarity(v1: np.ndarray, v2: np.ndarray) -> float:
        """
        Compute cosine similarity between two normalized vectors.
        """
        return float(np.dot(v1, v2))