from pydantic import BaseModel


class StartHumidifierResponse(BaseModel):
    message: str


class StopHumidifierResponse(BaseModel):
    message: str
