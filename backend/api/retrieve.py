from fastapi import APIRouter
from fastapi.responses import JSONResponse
from db.crud import get_articles

router = APIRouter()

@router.get("/retrieve")
async def retrieve_events():
    """
    Retrieve all accepted events, sorted by published_at (descending).
    
    Parameters:
        None
        
    Returns:
        JSONResponse: A JSON array of event objects sorted by published_at in descending order.
    """
    try :
        
        articles_relevant = get_articles()
        sorted_events = sorted(articles_relevant, key=lambda x: x['published_at'],reverse=True)
        
        return JSONResponse(content=sorted_events)
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": f"An error occurred while retrieving events: {str(e)}"}
        )
    
    
