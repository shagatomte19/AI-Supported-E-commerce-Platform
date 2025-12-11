def build_context(results: list) -> str:
    # TODO: token budgeting and attribution
    return "\n".join([r["doc"] for r in results])

