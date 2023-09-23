from typing import Literal

from fastapi import APIRouter, Depends

from drivers.balloon import BalloonDriver
from middlewares.verify_token import verify_token_middleware
from schemas.balloon import (
    BalloonNeedleRequest,
    BalloonNeedleResponse,
    BalloonStatusResponse,
)
from schemas.token import TokenRequestHeader

router = APIRouter(
    prefix="/balloon", tags=["balloon"], dependencies=[Depends(verify_token_middleware)]
)


@router.get("/status", response_model=BalloonStatusResponse)
def status_balloon(
    balloon_id: Literal[1, 2],
    UYUNPUNION_TOKEN: str = TokenRequestHeader(),
    driver: BalloonDriver = Depends(),
) -> BalloonStatusResponse:
    """
    風船の状態を取得する
    """
    driver.status(balloon_id=balloon_id)
    return BalloonStatusResponse(balloon_1=True, balloon_2=False)


@router.post("/needle", response_model=BalloonNeedleResponse)
def needle_balloon(
    req: BalloonNeedleRequest,
    UYUNPUNION_TOKEN: str = TokenRequestHeader(),
    driver: BalloonDriver = Depends(),
) -> BalloonNeedleResponse:
    """
    風船に針を刺す
    """
    driver.needle(balloon_id=req.balloon_id)
    return BalloonNeedleResponse(message="balloon needle")
