import azure.functions as func
from api.ingest import ingest_articles
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        articles = req.get_json()
        success = ingest_articles(articles)
        if success:
            return func.HttpResponse(
                json.dumps({"message": "Articles ingested successfully."}),
                status_code=200,
                mimetype="application/json"
            )
        else:
            return func.HttpResponse(
                json.dumps({"error": "Error ingesting articles."}),
                status_code=400,
                mimetype="application/json"
            )
    except Exception as e:
        return func.HttpResponse(
            json.dumps({"error": str(e)}),
            status_code=400,
            mimetype="application/json"
        )
