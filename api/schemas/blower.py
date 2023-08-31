from pydantic import BaseModel


class StartBlowerResponse(BaseModel):
    message: str


class StopBlowerResponse(BaseModel):
    message: str
