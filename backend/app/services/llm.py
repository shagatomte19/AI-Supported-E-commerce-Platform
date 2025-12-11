from datetime import datetime
from typing import Dict

from ..config import Settings
from ..dependencies import get_settings


def build_prompt(context: str, intent_label: str, settings: Settings) -> str:
    """Build a simple prompt for the downstream LLM."""
    return (
        f"Intent: {intent_label}\n"
        f"Model: {settings.llm_model}\n"
        f"Context:\n{context}\n"
        "Provide a concise, helpful answer for the shopper."
    )


def generate(context: str, intent_label: str) -> Dict[str, str]:
    """Return a deterministic mock LLM completion."""
    settings = get_settings()
    prompt = build_prompt(context, intent_label, settings)
    answer = (
        f"I am using {settings.llm_model} to help you with {intent_label}. "
        f"Based on our knowledge base, here is what I found:\n{context}"
    )
    return {
        "prompt": prompt,
        "completion": answer,
        "model": settings.llm_model,
        "created": datetime.utcnow().isoformat(),
    }

