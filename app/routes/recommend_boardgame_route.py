from flask import request
import json
from models.recommend import service_recommend


def manage_route(app):
    @app.post("/boardgames-recommend")
    def boardgames_recommend():
        body = request.get_json()
        result = service_recommend(body)
        result = json.loads(result.to_json())
        return result
