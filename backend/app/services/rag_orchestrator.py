from . import preprocess, intent, retriever, rerank, context_opt, llm


async def run_pipeline(query: str) -> dict:
    cleaned = preprocess.clean(query)
    intent_label = intent.classify(cleaned)
    retrieved = retriever.search(cleaned)
    ranked = rerank.rank(retrieved)
    context = context_opt.build_context(ranked)
    response = llm.generate(context, intent_label)
    return {
        "intent": intent_label,
        "response": response,
        "context_sources": ranked,
    }

