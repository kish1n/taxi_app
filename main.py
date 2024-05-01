import asyncio
from fastapi import FastAPI
from fastapi_users import fastapi_users, FastAPIUsers

from components.auth.manager import get_user_manager
from components.auth.schemas import UserRead, UserCreate
from components.maps import maps_get
from models.func import Core
from components.auth.auth import auth_backend
from models.models import User

app = FastAPI(
    title="Taxi 1488",
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(maps_get.router)

@app.get("/")
async def read_root():
    await Core.create_tables()
    return {"message": "Taxi 1488"}

#uvicorn main:app --reload
