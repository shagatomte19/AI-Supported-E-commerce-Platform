import base64
import gzip
from io import BytesIO


def compress(text: str) -> str:
    """Compress text with gzip and return base64 string."""
    buffer = BytesIO()
    with gzip.GzipFile(fileobj=buffer, mode="wb") as gz:
        gz.write(text.encode("utf-8"))
    return base64.b64encode(buffer.getvalue()).decode("utf-8")


def decompress(encoded: str) -> str:
    """Reverse compression back to plain text."""
    raw = base64.b64decode(encoded.encode("utf-8"))
    with gzip.GzipFile(fileobj=BytesIO(raw), mode="rb") as gz:
        return gz.read().decode("utf-8")

