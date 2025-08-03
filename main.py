import json
from src.pipelines import hierarchical_summary

if __name__ == "__main__":
    # Example input thread (could load from JSON later)
    comments = [
        "I think electric cars are the future, they reduce emissions."
    ]

    result = hierarchical_summary(comments, num_clusters=3)

    print("\n=== Thread-level Summary ===")
    print(result['thread_summary'])

    print("\n=== Cluster Summaries ===")
    for cid, summary in result['cluster_summaries'].items():
        print(f"Cluster {cid}: {summary}")