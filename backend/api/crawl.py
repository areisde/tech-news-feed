from fastapi import APIRouter
from backend.services.crawler import crawl_all_sources
from backend.api.ingest import process_articles
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/crawl")
async def crawl_and_process():
    """
    Crawl all sources, process articles using the ingest logic, and return relevant articles.

    Returns:
        200: JSON array of processed relevant articles.

    Example response:
    {
        "processed": [
            {
                "id": "string",
                "title": "string",
                "body": "string",
                "published_at": "2025-07-10T00:00:00Z",
                "embedding": [0.1, 0.2, ...]
            },
            ...
        ]
    }
    """
    articles = crawl_all_sources()
    process_articles(articles)
    return JSONResponse(
        status_code=200,
        content={"message": "Articles ingested successfully."}
    )
