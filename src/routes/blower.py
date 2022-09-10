from fastapi import APIRouter, Depends
from manipulator.blower import BlowerManipulator
from shemas.blower import StartBlowerrResponse, StopBlowerrResponse

router = APIRouter(prefix="/blower", tags=["blower"])


@router.post("/start", response_model=StartBlowerrResponse)
def start_blower(manipulator: BlowerManipulator = Depends()):
    """
    ブロワーを作動させる
    """
    return {"message": "pong"}


@router.post("/stop", response_model=StopBlowerrResponse)
def stop_blower(manipulator: BlowerManipulator = Depends()):
    """
    ブロワーを停止する
    """
    return {"message": "pong"}
