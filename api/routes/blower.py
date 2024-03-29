from fastapi import APIRouter, Depends

from drivers.blower import BlowerDriver
from middlewares.verify_token import verify_token_middleware
from schemas.blower import BlowerStartResponse, BlowerStopResponse
from schemas.token import TokenRequestHeader

router = APIRouter(
    prefix="/blower", tags=["blower"], dependencies=[Depends(verify_token_middleware)]
)


@router.post("/start", response_model=BlowerStartResponse)
def start_blower(
    UYUNPUNION_TOKEN: str = TokenRequestHeader(),
    driver: BlowerDriver = Depends(),
) -> BlowerStartResponse:
    """
    ブロワーを作動させる
    """
    driver.start()
    return BlowerStartResponse(message="blower started")


@router.post("/stop", response_model=BlowerStopResponse)
def stop_blower(
    UYUNPUNION_TOKEN: str = TokenRequestHeader(),
    driver: BlowerDriver = Depends(),
) -> BlowerStopResponse:
    """
    ブロワーを停止する
    """
    driver.stop()
    return BlowerStopResponse(message="blower stopped")
