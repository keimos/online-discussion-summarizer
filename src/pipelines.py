from typing import List, Dict
from .clustering import cluster_comments
from .summarizer import Summarizer

def hierarchical_summary(comments: List[str], num_clusters: int = 3) -> Dict:
    # Step 1: Cluster comments
    clusters = cluster_comments(comments, num_clusters)

    # Step 2: Summarize each cluster
    summarizer = Summarizer()
    cluster_summaries = {k: summarizer.summarize(" ".join(v)) for k, v in clusters.items()}

    # Step 3: Create a final summary of cluster summaries
    combined_text = " ".join(cluster_summaries.values())
    thread_summary = summarizer.summarize(combined_text, max_length=120, min_length=40)

    return {
        "thread_summary": thread_summary,
        "cluster_summaries": cluster_summaries
    }
