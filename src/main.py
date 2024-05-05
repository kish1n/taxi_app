from fastapi import FastAPI
from fastapi_users import FastAPIUsers

from src.auth.manager import get_user_manager
from src.auth.schemas import UserRead, UserCreate

from src.func import Core
from src.auth.base_config import auth_backend
from src.auth.models import User

from src.offer.router import router as offer_router
from src.pages.router import router as pg_router
from src.driver.router import router as user_router

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

app.include_router(pg_router)
app.include_router(offer_router)
app.include_router(user_router)

@app.get("/")
async def read_root():
    #await Core.create_tables()
    return {"message": "Taxi 1488"}

'''uvicorn src.main:app --reload'''
