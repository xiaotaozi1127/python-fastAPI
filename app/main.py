from fastapi import FastAPI
from app.api.routes import api_router
from app.api.health import router as health_router

app = FastAPI(
    title="My FastAPI Service",
    version="0.1.0",
)

app.include_router(api_router)
app.include_router(health_router)

