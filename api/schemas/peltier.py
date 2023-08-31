from pydantic import BaseModel


class ColdPeltierResponse(BaseModel):
    message: str


class WarmPeltierResponse(BaseModel):
    message: str


class StopPeltierResponse(BaseModel):
    message: str
