import asyncio

from backend.app.services.rag_orchestrator import run_pipeline


def test_chat_pipeline_runs():
    result = asyncio.run(run_pipeline("Where is my order?"))
    assert "intent" in result
    assert "answer" in result

