from fastapi import APIRouter, Depends
from ..dependencies import get_settings
from ..config import Settings

router = APIRouter()


@router.post("/")
async def chat_query(payload: dict, settings: Settings = Depends(get_settings)) -> dict:
    # TODO: wire to RAG orchestrator
    return {"echo": payload, "model": settings.llm_model}

