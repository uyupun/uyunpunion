from fastapi import APIRouter

router = APIRouter(prefix="/ping", tags=["other"])


@router.get("")
def ping():
    """
    APIへの疎通確認
    """
    return {"message": "pong"}
