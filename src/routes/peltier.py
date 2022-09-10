from fastapi import APIRouter, Depends
from manipulators.peltier import PeltierManipulator
from shemas.peltier import ColdPeltierResponse, StopPeltierResponse, WarmPeltierResponse

router = APIRouter(prefix="/peltier", tags=["peltier"])


@router.post("/cold", response_model=ColdPeltierResponse)
def cold_peltier(manipulator: PeltierManipulator = Depends()):
    """
    ペルチェ素子を冷却する
    """
    print("pepepepepeep")
    return {"message": "pong"}


@router.post("/warm", response_model=WarmPeltierResponse)
def warm_peltier(manipulator: PeltierManipulator = Depends()):
    """
    ペルチェ素子を加熱する
    """
    return {"message": "pong"}


@router.post("/stop", response_model=StopPeltierResponse)
def stop_peltier(manipulator: PeltierManipulator = Depends()):
    """
    ペルチェ素子を停止する
    """
    return {"message": "pong"}
