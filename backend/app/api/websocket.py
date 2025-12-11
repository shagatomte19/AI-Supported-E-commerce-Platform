from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from ..services import rag_orchestrator

router = APIRouter()


@router.websocket("/chat")
async def chat_ws(websocket: WebSocket) -> None:
    await websocket.accept()
    await websocket.send_json({"status": "connected"})
    try:
        while True:
            payload = await websocket.receive_text()
            result = await rag_orchestrator.run_pipeline(payload)
            await websocket.send_json(
                {
                    "intent": result["intent"],
                    "answer": result["answer"],
                    "model": result["model"],
                }
            )
    except WebSocketDisconnect:
        await websocket.close()

