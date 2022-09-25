from fastapi import APIRouter, Depends
from manipulators.blower import BlowerManipulator
from middlewares.verify_token import verify_token_middleware
from settings import get_settings
from shemas.blower import StartBlowerResponse, StopBlowerResponse
from shemas.token import TokenRequestHeader

router = APIRouter(
    prefix="/blower", tags=["blower"], dependencies=[Depends(verify_token_middleware)]
)


@router.post("/start", response_model=StartBlowerResponse)
def start_blower(
    UYUNPUNION_TOKEN: str = TokenRequestHeader(),
    manipulator: BlowerManipulator = Depends(),
):
    """
    ブロワーを作動させる
    """
    if get_settings().ENV == "prod":
        manipulator.start()
    return {"message": "pong"}


@router.post("/stop", response_model=StopBlowerResponse)
def stop_blower(
    UYUNPUNION_TOKEN: str = TokenRequestHeader(),
    manipulator: BlowerManipulator = Depends(),
):
    """
    ブロワーを停止する
    """
    if get_settings().ENV == "prod":
        manipulator.stop()
    return {"message": "pong"}
