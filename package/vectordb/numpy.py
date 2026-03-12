import numpy as np

class SimpleVectorDB:
    def __init__(self):
        self.vectors = []
        self.metadata = []

    def add(self, vector, meta):
        self.vectors.append(vector)
        self.metadata.append(meta)

    def search(self, query, top_k=3):
        # Convert list to matrix
        mat = np.array(self.vectors)       # shape (N, D)
        query = np.array(query)            # shape (D,)

        # cosine similarity
        sims = mat @ query / (
            np.linalg.norm(mat, axis=1) * np.linalg.norm(query)
        )

        # get top-k
        idx = np.argsort(-sims)[:top_k]
        return [(self.metadata[i], float(sims[i])) for i in idx]