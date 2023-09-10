from pydantic import BaseModel


class BlowerStartResponse(BaseModel):
    message: str


class BlowerStopResponse(BaseModel):
    message: str
