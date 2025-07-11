import azure.functions as func
from api.retrieve import retrieve_events
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        result = retrieve_events()
        return func.HttpResponse(
            json.dumps(result),
            status_code=200,
            mimetype="application/json"
        )
    except Exception as e:
        return func.HttpResponse(
            json.dumps({"error": str(e)}),
            status_code=500,
            mimetype="application/json"
        )
