from typing import List


def rank(results: List[dict], top_n: int = 5) -> List[dict]:
    """Sort results by score descending."""
    sorted_results = sorted(results, key=lambda r: r.get("score", 0), reverse=True)
    return sorted_results[:top_n]

