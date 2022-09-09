from dotenv import load_dotenv
from pydantic import BaseSettings


load_dotenv()


class Settings(BaseSettings):
    PROJECT_NAME: str = "汎用五感伝達機構 ウユンプニオン 零号機"
    VERSION: str = "0.0.0"

    class Config:
        env_file = ".env"


def get_settings():
    return Settings()
