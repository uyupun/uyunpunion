from drivers.humidifier import HumidifierDriver
from fastapi import APIRouter, Depends
from middlewares.verify_token import verify_token_middleware
from settings import get_settings
from schemas.humidifier import StartHumidifierResponse, StopHumidifierResponse
from schemas.token import TokenRequestHeader

router = APIRouter(
    prefix="/humidifier",
    tags=["humidifier"],
    dependencies=[Depends(verify_token_middleware)],
)


@router.post("/start", response_model=StartHumidifierResponse)
def start_humidifier(
    UYUNPUNION_TOKEN: str = TokenRequestHeader(),
    driver: HumidifierDriver = Depends(),
):
    """
    加湿器を作動させる
    """
    if get_settings().ENV == "prod":
        driver.start()
    return {"message": "pong"}


@router.post("/stop", response_model=StopHumidifierResponse)
def stop_humidifier(
    UYUNPUNION_TOKEN: str = TokenRequestHeader(),
    driver: HumidifierDriver = Depends(),
):
    """
    加湿器を停止する
    """
    if get_settings().ENV == "prod":
        driver.stop()
    return {"message": "pong"}
