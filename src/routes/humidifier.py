from fastapi import APIRouter, Depends
from manipulators.humidifier import HumidifierManipulator
from middlewares.verify_token import verify_token_middleware
from shemas.humidifier import StartHumidifierResponse, StopHumidifierResponse
from shemas.token import TokenRequestHeader

router = APIRouter(
    prefix="/humidifier",
    tags=["humidifier"],
    dependencies=[Depends(verify_token_middleware)],
)


@router.post("/start", response_model=StartHumidifierResponse)
def start_blower(
    UYUNPUNION_TOKEN: str = TokenRequestHeader(),
    manipulator: HumidifierManipulator = Depends(),
):
    """
    加湿器を作動させる
    """
    return {"message": "pong"}


@router.post("/stop", response_model=StopHumidifierResponse)
def stop_blower(
    UYUNPUNION_TOKEN: str = TokenRequestHeader(),
    manipulator: HumidifierManipulator = Depends(),
):
    """
    加湿器を停止する
    """
    return {"message": "pong"}
