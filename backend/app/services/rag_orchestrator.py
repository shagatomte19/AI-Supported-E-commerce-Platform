from typing import Any, Dict

from ..cache import redis_cache
from ..utils import logging, monitoring
from . import context_opt, intent, llm, preprocess, rerank, retriever

logger = logging.setup_logging(__name__)


async def run_pipeline(query: str) -> Dict[str, Any]:
    """Execute the RAG pipeline end-to-end."""
    cache_key = f"rag:{query}"
    cached = redis_cache.get(cache_key)
    if cached:
        monitoring.record_metric("rag_cache_hit", 1.0)
        return cached

    cleaned = preprocess.clean(query)
    intent_label = intent.classify(cleaned)
    retrieved = retriever.search(cleaned)
    ranked = rerank.rank(retrieved)
    context = context_opt.build_context(ranked)
    llm_result = llm.generate(context, intent_label)

    result = {
        "intent": intent_label,
        "answer": llm_result["completion"],
        "prompt": llm_result["prompt"],
        "model": llm_result["model"],
        "context_sources": ranked,
    }

    redis_cache.set(cache_key, result)
    monitoring.record_metric("rag_cache_hit", 0.0)
    monitoring.record_metric("rag_results", len(ranked))
    logger.info("RAG pipeline completed", extra={"intent": intent_label})
    return result

