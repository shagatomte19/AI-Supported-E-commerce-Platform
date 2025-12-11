from fastapi import FastAPI
from .api import chat, websocket, admin


def create_app() -> FastAPI:
    app = FastAPI(title="AI-Supported E-commerce Platform", version="0.1.0")

    @app.get("/health")
    def health() -> dict:
        return {"status": "ok"}

    app.include_router(chat.router, prefix="/api/chat", tags=["chat"])
    app.include_router(admin.router, prefix="/api/admin", tags=["admin"])
    app.include_router(websocket.router, prefix="/ws", tags=["ws"])
    return app


app = create_app()
