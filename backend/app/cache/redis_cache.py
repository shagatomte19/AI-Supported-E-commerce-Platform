import time
from typing import Any, Dict, Tuple

_cache: Dict[str, Tuple[Any, float]] = {}


def set(key: str, value, ttl: int = 300) -> None:
    expires_at = time.time() + ttl
    _cache[key] = (value, expires_at)


def get(key: str):
    item = _cache.get(key)
    if not item:
        return None
    value, expires_at = item
    if time.time() > expires_at:
        _cache.pop(key, None)
        return None
    return value


def delete(key: str) -> None:
    _cache.pop(key, None)

