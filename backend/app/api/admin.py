from fastapi import APIRouter

router = APIRouter()


@router.get("/metrics")
async def metrics() -> dict:
    # TODO: expose Prometheus metrics
    return {"metrics": "not-implemented"}

