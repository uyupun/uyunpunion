from fastapi import FastAPI

from settings import get_settings
from routes import ping


settings = get_settings()


def init_app(app: FastAPI) -> FastAPI:
    register_routes(app)
    return app


def register_routes(app: FastAPI) -> None:
    app.include_router(ping.router)


app = init_app(FastAPI(
    title=settings.PROJECT_NAME,
    description="ウユンプニオン・インタフェースのAPI仕様書",
    version=settings.VERSION,
))
