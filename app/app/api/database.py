from fastapi import APIRouter, Depends, HTTPException, Request
from pymongo import mongo_client

from .auth import manager
from .settings import ENV


client = mongo_client.MongoClient(ENV.DATABASE_URL)
db = client[ENV.MAIN_DATABASE]

database_route = APIRouter()


@database_route.post("/users")
async def users_find(request: Request, user=Depends(manager)):
    query = await request.json()

    user = db.users.find_one(query)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return user_helper(db.users.find_one(query))


def user_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "username": str(user["username"]),
        "password": str(user["password"]),
    }
