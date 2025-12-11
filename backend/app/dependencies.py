from functools import lru_cache
from typing import Generator

from sqlalchemy.orm import Session

from .config import Settings
from .db.postgres import SessionLocal


@lru_cache
def get_settings() -> Settings:
    return Settings()


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

