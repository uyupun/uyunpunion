from functools import lru_cache

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    PROJECT_NAME: str = "汎用五感伝達機構 ウユンプニオン 零号機"
    DESCRIPTION: str = "五感に多彩な刺激を与えるためのインタフェースを提供します"

    ENV: str
    VERSION: str
    UYUNPUNION_TOKEN: str

    ADDRESS: str
    PORT: int

    class Config:
        env_file: str = ".env"


@lru_cache
def get_settings():
    return Settings()  # type: ignore
