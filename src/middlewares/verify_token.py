import secrets
from typing import Callable

from fastapi import Request, Response
from fastapi.responses import JSONResponse
from settings import get_settings
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED


class VerifyTokenMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        settings = get_settings()

        if "UYUNPUNION-TOKEN" not in request.headers:
            return JSONResponse(content={}, status_code=HTTP_400_BAD_REQUEST)

        if not secrets.compare_digest(
            settings.UYUNPUNION_TOKEN, request.headers["UYUNPUNION-TOKEN"]
        ):
            return JSONResponse(content={}, status_code=HTTP_401_UNAUTHORIZED)

        response = await call_next(request)
        return response
