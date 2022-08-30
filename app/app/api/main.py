from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from .auth import auth_route
from .database import database_route
from .settings import TEMPLATES


app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(auth_route, prefix="/auth")


@app.get("/")
async def homepage(request: Request):
    return TEMPLATES.TemplateResponse("pages/index.html", {"request": request})


@app.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    return TEMPLATES.TemplateResponse("login.html", {"request": request})
