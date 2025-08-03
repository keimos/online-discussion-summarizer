import numpy as np
from typing import List, Dict
from sklearn.cluster import KMeans
from sentence_transformers import SentenceTransformer

embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

def cluster_comments(sentences: List[str], num_clusters: int = 3, random_state: int = 42) -> Dict[int, List[str]]:
    embeddings = embedding_model.encode(comments)
    kmeans = KMeans(n_clusters=num_clusters, random_state=random_state)
    labels = kmeans.fit_predict(embeddings)

    clustered = {}
    for idx, label in enumerate(labels):
        clustered.setdefault(label, []).append(sentences[idx])

    return clustered