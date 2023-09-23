from typing import Literal

from pydantic import BaseModel, conint


class BalloonStatusResponse(BaseModel):
    balloon_1: bool
    balloon_2: bool


class BalloonNeedleRequest(BaseModel):
    balloon_id: Literal[1, 2]
    power: conint(gt=0)  # type: ignore


class BalloonNeedleResponse(BaseModel):
    message: str
