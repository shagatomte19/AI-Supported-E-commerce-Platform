import difflib
from typing import List

from backend.data.data import corpus


def _score(doc: str, query: str) -> float:
    return difflib.SequenceMatcher(None, doc.lower(), query.lower()).ratio()


def search(query: str, top_k: int = 5) -> List[dict]:
    """Hybrid search across FAQs and product blurbs."""
    docs = corpus()
    scored = []
    for item in docs:
        doc_text = f"{item['title']} {item['body']}"
        score = _score(doc_text, query)
        scored.append(
            {
                "id": item["id"],
                "type": item["type"],
                "doc": doc_text,
                "score": score,
            }
        )
    scored.sort(key=lambda r: r["score"], reverse=True)
    return scored[:top_k]

