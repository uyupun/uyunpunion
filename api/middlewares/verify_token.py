import secrets

from fastapi import HTTPException, Request
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED

from settings import get_settings


async def verify_token_middleware(request: Request):
    settings = get_settings()

    if "UYUNPUNION-TOKEN" not in request.headers:
        raise HTTPException(detail={}, status_code=HTTP_400_BAD_REQUEST)

    if not secrets.compare_digest(
        settings.UYUNPUNION_TOKEN, request.headers["UYUNPUNION-TOKEN"]
    ):
        raise HTTPException(detail={}, status_code=HTTP_401_UNAUTHORIZED)
