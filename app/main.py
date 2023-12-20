from flask import Flask
from dotenv import load_dotenv
import os

# config env variable
load_dotenv()

# routes
import routes.recommend_boardgame_route as recommend_boardgame_route

app = Flask(__name__)


@app.get("/")
def index():
    return {
        "api_name": "Boardgame Recommend Service",
        "api_version": "1.0.0",
        "api_released": "2023-19-12 14:59:00",
        "api_documentation": None,
        "api_status": "active",
    }


# router
recommend_boardgame_route.manage_route(app)

if __name__ == "__main__":
    app.run(port=int(os.getenv("PORT")))

# flask --app ./app/main.py run --debug -p 5001
# black ./app/*
