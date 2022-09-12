from fastapi import APIRouter, Depends
from manipulators.peltier import PeltierManipulator
from middlewares.verify_token import verify_token_middleware
from shemas.peltier import ColdPeltierResponse, StopPeltierResponse, WarmPeltierResponse
from shemas.token import TokenRequestHeader

router = APIRouter(
    prefix="/peltier", tags=["peltier"], dependencies=[Depends(verify_token_middleware)]
)


@router.post("/cold", response_model=ColdPeltierResponse)
def cold_peltier(
    UYUNPUNION_TOKEN: str = TokenRequestHeader(),
    manipulator: PeltierManipulator = Depends(),
):
    """
    ペルチェ素子を冷却する
    """
    return {"message": "pong"}


@router.post("/warm", response_model=WarmPeltierResponse)
def warm_peltier(
    UYUNPUNION_TOKEN: str = TokenRequestHeader(),
    manipulator: PeltierManipulator = Depends(),
):
    """
    ペルチェ素子を加熱する
    """
    return {"message": "pong"}


@router.post("/stop", response_model=StopPeltierResponse)
def stop_peltier(
    UYUNPUNION_TOKEN: str = TokenRequestHeader(),
    manipulator: PeltierManipulator = Depends(),
):
    """
    ペルチェ素子を停止する
    """
    return {"message": "pong"}
