from fastapi import APIRouter

health_router = APIRouter()

@health_router.get("/health")
def health_check():
    """
    Health check endpoint.
    Used by monitoring / load balancers.
    """
    return {"status": "ok"}
