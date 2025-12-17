from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def health_check():
    """
    Health check endpoint.
    Used by monitoring / load balancers.
    """
    return {"status": "ok"}
