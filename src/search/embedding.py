from typing import List
import numpy as np
from sentence_transformers import SentenceTransformer

def dummy_embedding(text: str) -> np.ndarray:
    """
    Very naive embedding: convert characters to numeric values.
    For demonstration only.
    """
    return np.array([ord(c) for c in text[:10]], dtype=float)


class EmbeddingService:
    """
    Responsible only for converting text into vector embeddings.
    """

    def __init__(self, model_name: str = "all-MiniLM-L6-v2") -> None:
        self._model = SentenceTransformer(model_name)

    def embed(self, texts: List[str]) -> np.ndarray:
        """
        Convert list of texts into embedding vectors.
        """
        if not texts:
            raise ValueError("Input texts must not be empty.")

        return np.array(self._model.encode(texts, normalize_embeddings=True))