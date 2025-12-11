from fastapi import APIRouter

from ..utils import monitoring

router = APIRouter()


@router.get("/metrics")
async def metrics() -> dict:
    return {"metrics": monitoring.get_metrics()}

