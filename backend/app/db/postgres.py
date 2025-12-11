from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from ..config import Settings

Base = declarative_base()


def get_engine():
    settings = Settings()
    return create_engine(settings.postgres_url, future=True)


Engine = get_engine()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=Engine)

