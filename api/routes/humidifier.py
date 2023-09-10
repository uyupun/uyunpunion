from fastapi import APIRouter, Depends

from drivers.humidifier import HumidifierDriver
from middlewares.verify_token import verify_token_middleware
from schemas.humidifier import HumidifierStartResponse, HumidifierStopResponse
from schemas.token import TokenRequestHeader
from settings import get_settings

router = APIRouter(
    prefix="/humidifier",
    tags=["humidifier"],
    dependencies=[Depends(verify_token_middleware)],
)


@router.post("/start", response_model=HumidifierStartResponse)
def start_humidifier(
    UYUNPUNION_TOKEN: str = TokenRequestHeader(),
    driver: HumidifierDriver = Depends(),
) -> HumidifierStartResponse:
    """
    加湿器を作動させる
    """
    if get_settings().ENV == "prod":
        driver.start()
    return HumidifierStartResponse(message="pong")


@router.post("/stop", response_model=HumidifierStopResponse)
def stop_humidifier(
    UYUNPUNION_TOKEN: str = TokenRequestHeader(),
    driver: HumidifierDriver = Depends(),
) -> HumidifierStopResponse:
    """
    加湿器を停止する
    """
    if get_settings().ENV == "prod":
        driver.stop()
    return HumidifierStopResponse(message="pong")
