from functools import lru_cache

from dotenv import load_dotenv
from pydantic import constr
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    PROJECT_NAME: str = "汎用五感伝達機構 ウユンプニオン 一号機"
    DESCRIPTION: str = "五感に多彩な刺激を与えるためのインタフェースを提供します"

    ENV: constr(pattern="^(dev|prod)$")  # type: ignore # noqa: F722
    VERSION: str
    UYUNPUNION_TOKEN: str

    ADDRESS: str
    PORT: int

    class Config:
        env_file: str = ".env"
        extra: str = "ignore"


@lru_cache
def get_settings() -> Settings:
    return Settings()  # type: ignore
