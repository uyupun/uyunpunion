import uvicorn
from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware

from middlewares.verify_token import verify_token
from routes import blower, peltier, ping
from settings import get_settings

settings = get_settings()


def init_app(app: FastAPI) -> FastAPI:
    app.add_middleware(BaseHTTPMiddleware, dispatch=verify_token)
    register_routes(app)
    return app


def register_routes(app: FastAPI) -> None:
    app.include_router(ping.router)
    app.include_router(peltier.router)
    app.include_router(blower.router)


app = init_app(
    FastAPI(
        title=settings.PROJECT_NAME,
        description=settings.DESCRIPTION,
        version=settings.VERSION,
    )
)

if __name__ == "__main__":
    uvicorn.run("app:app", port=settings.PORT, reload=True)
