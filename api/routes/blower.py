from drivers.blower import BlowerDriver
from fastapi import APIRouter, Depends
from middlewares.verify_token import verify_token_middleware
from settings import get_settings
from schemas.blower import StartBlowerResponse, StopBlowerResponse
from schemas.token import TokenRequestHeader

router = APIRouter(
    prefix="/blower", tags=["blower"], dependencies=[Depends(verify_token_middleware)]
)


@router.post("/start", response_model=StartBlowerResponse)
def start_blower(
    UYUNPUNION_TOKEN: str = TokenRequestHeader(),
    driver: BlowerDriver = Depends(),
):
    """
    ブロワーを作動させる
    """
    if get_settings().ENV == "prod":
        driver.start()
    return {"message": "pong"}


@router.post("/stop", response_model=StopBlowerResponse)
def stop_blower(
    UYUNPUNION_TOKEN: str = TokenRequestHeader(),
    driver: BlowerDriver = Depends(),
):
    """
    ブロワーを停止する
    """
    if get_settings().ENV == "prod":
        driver.stop()
    return {"message": "pong"}
