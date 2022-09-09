from dotenv import load_dotenv
from pydantic import BaseSettings


load_dotenv()


class Settings(BaseSettings):
    PROJECT_NAME: str = "uyunpunion"

    class Config:
        env_file = ".env"


def get_settings():
    return Settings()
