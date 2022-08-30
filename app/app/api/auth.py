from fastapi import APIRouter, Depends
from fastapi_login import LoginManager
from fastapi_login.exceptions import InvalidCredentialsException
from fastapi.security import OAuth2PasswordRequestForm

from .settings import ENV


auth_route = APIRouter()
manager = LoginManager(ENV.SECRET_KEY, token_url="/auth/token")


@auth_route.post("/token")
def generate_token(data: OAuth2PasswordRequestForm = Depends()):
    username = data.username
    password = data.password

    user = load_user(username)
    print(user)
    if not user:
        raise InvalidCredentialsException
    elif password != user["password"]:
        raise InvalidCredentialsException

    access_token = manager.create_access_token(data=dict(sub=username))
    return {"access_token": access_token, "token_type": "bearer"}


@manager.user_loader()
def load_user(username):
    from .database import db

    return db["users"].find_one({"username": username})
