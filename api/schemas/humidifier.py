from pydantic import BaseModel


class HumidifierStartResponse(BaseModel):
    message: str


class HumidifierStopResponse(BaseModel):
    message: str
