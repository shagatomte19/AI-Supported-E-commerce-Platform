import logging
import os
from typing import Optional

DEFAULT_LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()


def setup_logging(name: str = "ai-support", level: Optional[str] = None) -> logging.Logger:
    """Configure and return a structured logger."""
    log_level = getattr(logging, (level or DEFAULT_LOG_LEVEL), logging.INFO)
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )
    return logging.getLogger(name)

