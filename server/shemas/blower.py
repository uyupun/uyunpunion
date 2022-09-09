from pydantic import BaseModel


class StartBlowerrResponse(BaseModel):
    message: str


class StopBlowerrResponse(BaseModel):
    message: str
