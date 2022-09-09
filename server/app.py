import uvicorn
from fastapi import FastAPI

from settings import get_settings
from routes import ping, peltier, blower


settings = get_settings()


def init_app(app: FastAPI) -> FastAPI:
    register_routes(app)
    return app


def register_routes(app: FastAPI) -> None:
    app.include_router(ping.router)
    app.include_router(peltier.router)
    app.include_router(blower.router)


app = init_app(FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.DESCRIPTION,
    version=settings.VERSION,
))


if __name__ == "__main__":
    uvicorn.run("app:app", port=settings.PORT, reload=True)
