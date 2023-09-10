from fastapi import APIRouter, Depends

from drivers.peltier import PeltierDriver, PeltierMode
from middlewares.verify_token import verify_token_middleware
from schemas.peltier import (
    PeltierColdResponse,
    PeltierStopResponse,
    PeltierWarmResponse,
)
from schemas.token import TokenRequestHeader
from settings import get_settings

router = APIRouter(
    prefix="/peltier", tags=["peltier"], dependencies=[Depends(verify_token_middleware)]
)


@router.post("/cold", response_model=PeltierColdResponse)
def cold_peltier(
    UYUNPUNION_TOKEN: str = TokenRequestHeader(),
    driver: PeltierDriver = Depends(),
) -> PeltierColdResponse:
    """
    ペルチェ素子を冷却する
    """
    if get_settings().ENV == "prod":
        driver.start(mode=PeltierMode.Cold)
    return PeltierColdResponse(message="pong")


@router.post("/warm", response_model=PeltierWarmResponse)
def warm_peltier(
    UYUNPUNION_TOKEN: str = TokenRequestHeader(),
    driver: PeltierDriver = Depends(),
) -> PeltierWarmResponse:
    """
    ペルチェ素子を加熱する
    """
    if get_settings().ENV == "prod":
        driver.start(mode=PeltierMode.Warm)
    return PeltierWarmResponse(message="pong")


@router.post("/stop", response_model=PeltierStopResponse)
def stop_peltier(
    UYUNPUNION_TOKEN: str = TokenRequestHeader(),
    driver: PeltierDriver = Depends(),
) -> PeltierStopResponse:
    """
    ペルチェ素子を停止する
    """
    if get_settings().ENV == "prod":
        driver.stop()
    return PeltierStopResponse(message="pong")
