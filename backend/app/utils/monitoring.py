from collections import defaultdict
from time import time
from typing import Dict, Tuple

_metrics: Dict[str, Tuple[float, float]] = defaultdict(lambda: (0.0, 0.0))


def record_metric(name: str, value: float) -> None:
    """Store latest value and timestamp for a metric."""
    _metrics[name] = (value, time())


def get_metrics() -> Dict[str, Tuple[float, float]]:
    """Return a snapshot of recorded metrics."""
    return dict(_metrics)

