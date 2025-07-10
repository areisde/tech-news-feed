from fastapi import FastAPI
from .ingest import router as ingest_router
from .retrieve import router as retrieve_router

app = FastAPI()
app.include_router(ingest_router)
app.include_router(retrieve_router)