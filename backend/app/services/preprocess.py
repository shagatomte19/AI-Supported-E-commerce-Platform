import re
from typing import List

STOPWORDS: List[str] = ["please", "kindly", "thanks", "thank", "hi", "hello"]


def normalize_whitespace(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def remove_stopwords(text: str) -> str:
    words = [w for w in text.split() if w.lower() not in STOPWORDS]
    return " ".join(words)


def clean(query: str) -> str:
    """Lightweight normalization before retrieval/classification."""
    normalized = normalize_whitespace(query)
    return remove_stopwords(normalized)

