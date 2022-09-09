from fastapi import FastAPI

from routes import ping


def init_app(app: FastAPI) -> FastAPI:
    register_routes(app)
    return app


def register_routes(app: FastAPI) -> None:
    app.include_router(ping.router)


app = init_app(FastAPI())
