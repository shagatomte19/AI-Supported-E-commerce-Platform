from typing import List


def build_context(results: List[dict], max_tokens: int = 3000) -> str:
    """Concatenate docs until a rough token budget is reached."""
    lines = []
    token_count = 0
    for item in results:
        doc = item.get("doc", "")
        doc_tokens = len(doc.split())
        if token_count + doc_tokens > max_tokens:
            break
        lines.append(doc)
        token_count += doc_tokens
    return "\n\n".join(lines)

