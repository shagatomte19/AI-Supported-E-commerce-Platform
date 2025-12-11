from typing import Dict

INTENT_KEYWORDS: Dict[str, tuple] = {
    "order_status": ("order", "status", "shipping", "delivery", "tracking"),
    "return": ("return", "refund", "exchange"),
    "product_info": ("specs", "size", "color", "compatibility", "product"),
    "support": ("help", "issue", "problem", "bug"),
}


def classify(query: str) -> str:
    """Rule-based intent classifier."""
    lower_q = query.lower()
    for intent, keywords in INTENT_KEYWORDS.items():
        if any(word in lower_q for word in keywords):
            return intent
    return "general_support"

