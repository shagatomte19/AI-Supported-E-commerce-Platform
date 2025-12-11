import difflib
from typing import Dict, List

_store: Dict[str, str] = {}


def upsert_vectors(items: List[dict]) -> None:
    """Store vector payloads in memory (placeholder for Qdrant)."""
    for item in items:
        _store[item["id"]] = item.get("text", "")


def search_similar(text: str, top_k: int = 3) -> List[dict]:
    """Return the most similar stored items."""
    scored = []
    for key, value in _store.items():
        score = difflib.SequenceMatcher(None, value.lower(), text.lower()).ratio()
        scored.append({"id": key, "text": value, "score": score})
    scored.sort(key=lambda r: r["score"], reverse=True)
    return scored[:top_k]

