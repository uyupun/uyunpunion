from pydantic import BaseModel


class PeltierColdResponse(BaseModel):
    message: str


class PeltierWarmResponse(BaseModel):
    message: str


class PeltierStopResponse(BaseModel):
    message: str
