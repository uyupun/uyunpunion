from fastapi import APIRouter


router = APIRouter(prefix="/peltier", tags=["peltier"])


@router.post("/cold")
def cold_peltier():
    """
    ペルチェ素子を冷却する
    """
    return {"message": "pong"}


@router.post("/warm")
def warm_peltier():
    """
    ペルチェ素子を加熱する
    """
    return {"message": "pong"}


@router.post("/stop")
def stop_peltier():
    """
    ペルチェ素子を停止する
    """
    return {"message": "pong"}
