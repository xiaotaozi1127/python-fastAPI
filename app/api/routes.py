from fastapi import APIRouter

api_router = APIRouter(prefix="/api")

@api_router.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}
