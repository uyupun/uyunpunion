from fastapi import APIRouter

router = APIRouter(prefix="/ping")

@router.get("")
def ping():
    """
    APIへの疎通確認用
    """
    return {"message": "pong"}
