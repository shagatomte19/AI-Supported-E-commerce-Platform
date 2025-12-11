from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from ..dependencies import get_settings

Base = declarative_base()


def get_engine():
    settings = get_settings()
    return create_engine(settings.postgres_url, future=True)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=get_engine())

