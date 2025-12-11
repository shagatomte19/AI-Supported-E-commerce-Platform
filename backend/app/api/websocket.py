from fastapi import APIRouter, WebSocket

router = APIRouter()


@router.websocket("/chat")
async def chat_ws(websocket: WebSocket) -> None:
    await websocket.accept()
    await websocket.send_json({"status": "connected"})
    await websocket.close()

