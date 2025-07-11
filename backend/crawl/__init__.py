import azure.functions as func
from api.crawl import crawl_and_process

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        result = crawl_and_process()
        return func.HttpResponse(
            str(result),
            status_code=200,
            mimetype="application/json"
        )
    except Exception as e:
        return func.HttpResponse(
            f"Error: {str(e)}",
            status_code=500
        )
