from fastapi import APIRouter, Depends

from drivers.balloon import BalloonDriver
from middlewares.verify_token import verify_token_middleware
from schemas.balloon import (
    BalloonNeedleRequest,
    BalloonNeedleResponse,
    BalloonStatusResponse,
)
from schemas.token import TokenRequestHeader
from sensor.balloon import (
    BalloonSensor,
    PlayerSide,
)

router = APIRouter(
    prefix="/balloon", tags=["balloon"], dependencies=[Depends(verify_token_middleware)]
)


@router.get("/status", response_model=BalloonStatusResponse)
def status_balloon(
    UYUNPUNION_TOKEN: str = TokenRequestHeader(),
    driver: BalloonDriver = Depends(),
) -> BalloonStatusResponse:
    """
    風船の状態を取得する
    """
    balloonSensorA = BalloonSensor(PlayerSide.A)
    balloonSensorB = BalloonSensor(PlayerSide.B)

    return BalloonStatusResponse(
        balloon_1=balloonSensorA.measure() > 1000,
        balloon_2=balloonSensorB.measure() > 1000,
    )


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
