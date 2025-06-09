import os
from dotenv import load_dotenv
from pydantic.v1 import BaseSettings

load_dotenv()


class Settings(BaseSettings):

    DB_HOST: str = os.environ.get("DB_HOST")
    DB_PORT: str = os.environ.get("DB_PORT")
    DB_NAME: str = os.environ.get("DB_NAME")
    DB_USER: str = os.environ.get("DB_USER")
    DB_PASS: str = os.environ.get("DB_PASS")
    db_url: str = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    EMAIL_ADDRESS: str = os.environ.get("EMAIL_ADDRESS")
    EMAIL_PASSWORD: str = os.environ.get("EMAIL_PASSWORD")
    MAIL_PORT: str = os.environ.get("MAIL_PORT")
    MAIL_SERVER: str = os.environ.get("MAIL_SERVER")
    MAIL_TLS: bool = os.environ.get("MAIL_TLS")
    MAIL_SSL: bool = os.environ.get("MAIL_SSL")
    USE_CREDENTIALS: bool = os.environ.get("USE_CREDENTIALS")

settings = Settings()