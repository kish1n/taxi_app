from fastapi import FastAPI
from fastapi_users import FastAPIUsers

from auth.manager import get_user_manager
from auth.schemas import UserRead, UserCreate

from func import Core
from auth.base_config import auth_backend
from auth.models import User

from offer.router import router as offer_router

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

app.include_router(offer_router)

@app.get("/")
async def read_root():
    await Core.create_tables()
    return {"message": "Taxi 1488"}

#uvicorn main:app --reload
