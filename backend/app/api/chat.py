from typing import Any, Dict

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field

from ..config import Settings
from ..dependencies import get_settings
from ..services import rag_orchestrator

router = APIRouter()


class ChatRequest(BaseModel):
    message: str = Field(..., description="User message to process")
    user_id: str | None = Field(None, description="Optional user identifier")


class ChatResponse(BaseModel):
    intent: str
    answer: str
    model: str
    context_sources: list[dict]


@router.post("/", response_model=ChatResponse)
async def chat_query(
    payload: ChatRequest, settings: Settings = Depends(get_settings)
) -> Dict[str, Any]:
    if not payload.message:
        raise HTTPException(status_code=400, detail="Message is required")
    rag_result = await rag_orchestrator.run_pipeline(payload.message)
    return {
        "intent": rag_result["intent"],
        "answer": rag_result["answer"],
        "model": settings.llm_model,
        "context_sources": rag_result["context_sources"],
    }

