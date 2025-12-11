from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api import admin, chat, websocket
from .db.postgres import Base, Engine
from .models import conversation, ticket, user  # noqa: F401 - register models
from .utils.logging import setup_logging

logger = setup_logging(__name__)


def create_app() -> FastAPI:
    app = FastAPI(title="AI-Supported E-commerce Platform", version="0.1.0")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.on_event("startup")
    def on_startup():
        Base.metadata.create_all(bind=Engine)
        logger.info("Database tables ensured")

    @app.get("/health")
    def health() -> dict:
        return {"status": "ok"}

    app.include_router(chat.router, prefix="/api/chat", tags=["chat"])
    app.include_router(admin.router, prefix="/api/admin", tags=["admin"])
    app.include_router(websocket.router, prefix="/ws", tags=["ws"])
    return app


app = create_app()
