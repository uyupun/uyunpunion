from fastapi import APIRouter
from shemas.blower import StartBlowerrResponse, StopBlowerrResponse

router = APIRouter(prefix="/blower", tags=["blower"])


@router.post("/start", response_model=StartBlowerrResponse)
def start_blower():
    """
    ブロワーを作動させる
    """
    return {"message": "pong"}


@router.post("/stop", response_model=StopBlowerrResponse)
def stop_blower():
    """
    ブロワーを停止する
    """
    return {"message": "pong"}
