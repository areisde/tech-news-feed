from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import List, Optional
from backend.db.crud import add_filter, get_similar_articles
from backend.services.embeddings import embed_text
from backend.services.filter import filter_article
from backend.db.models import Article
import logging

router = APIRouter()

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@router.post("/ingest")
async def ingest_articles(request: Request):
    """
    Ingest a batch of raw article objects as a JSON array in the request body.
    Each object must have id, source, title, body (optional), published_at.
    Returns HTTP 200 on success.
    
    Parameters:
        - articles : JSON array of articles to ingest.
    
    Request body example:
    [
        {
            "id": "string",
            "source": "string",
            "title": "string",
            "body": "string",
            "published_at": "2025-07-10T00:00:00Z"
        }
    ]

    Responses:
        200: Articles ingested successfully.
        400: Invalid request format.
    """
    # Parse the request body as a list of articles
    try:
        articles = await request.json()
        for article in articles:
            article_obj = Article(
                id=article.get("id"),
                source=article.get("source"),
                title=article.get("title"),
                body=article.get("body", ""),
                published_at=article.get("published_at"),
            )
            
            filter_article(article_obj)
    except Exception as e:
        logger.error(f"Error processing request: {e}")
        return JSONResponse(
            status_code=400,
            content={"error": "Invalid request format. Ensure you are sending a JSON array of articles."}
        )

    return JSONResponse(
        status_code=200,
        content={"message": "Articles ingested successfully."}
    )