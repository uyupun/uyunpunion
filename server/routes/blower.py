from fastapi import APIRouter


router = APIRouter(prefix="/blower", tags=["blower"])


@router.post("/start")
def start_blower():
    """
    ブロワーを作動させる
    """
    return {"message": "pong"}


@router.post("/stop")
def stop_blower():
    """
    ブロワーを停止する
    """
    return {"message": "pong"}
