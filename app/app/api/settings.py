from fastapi.templating import Jinja2Templates
import os


class Environment(BaseSettings):
    DATABASE_URL: str
    CLIENT_ORIGIN: str
    MAIN_DATABASE: str
    SECRET_KEY: str

    class Config:
        env_prefix = ""
        case_sentive = True
        env_file = "./../.env"
        env_file_encoding = "utf-8"


ENV = Environment()


APP_DIR = "app"
TEMPLATES_DIR = os.path.join(APP_DIR, "templates")

TEMPLATES = Jinja2Templates(directory=TEMPLATES_DIR)
