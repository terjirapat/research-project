from sentence_transformers import SentenceTransformer

class SimpleEmbedding:
    def __init__(self):
        self.model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')
    
    def run(self, sentence:list):
        embeddings = self.model.encode(sentence)
        return embeddings