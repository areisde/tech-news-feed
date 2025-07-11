from fastapi import FastAPI
from api.ingest import router as ingest_router
from api.retrieve import router as retrieve_router
from api.crawl import router as crawl_router

app = FastAPI()
app.include_router(ingest_router)
app.include_router(retrieve_router)
app.include_router(crawl_router)