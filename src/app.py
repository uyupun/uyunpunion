from fastapi import FastAPI

from routes import blower, humidifier, peltier, ping
from settings import get_settings

settings = get_settings()


def init_app(app: FastAPI) -> FastAPI:
    register_routes(app)
    return app


def register_routes(app: FastAPI) -> None:
    app.include_router(ping.router)
    app.include_router(peltier.router)
    app.include_router(blower.router)
    app.include_router(humidifier.router)


app = init_app(
    FastAPI(
        title=settings.PROJECT_NAME,
        description=settings.DESCRIPTION,
        version=settings.VERSION,
    )
)
