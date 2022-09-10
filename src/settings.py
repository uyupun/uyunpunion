from functools import lru_cache
from typing import Optional

from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    PROJECT_NAME: str = "汎用五感伝達機構 ウユンプニオン 零号機"
    DESCRIPTION: str = "五感に多彩な刺激を与えるためのインタフェースを提供します"
    VERSION: str = "0.0.0"

    PORT: Optional[int] = 8080
    UYUNPUNION_TOKEN: str

    class Config:
        env_file: str = ".env"


@lru_cache
def get_settings():
    return Settings()
