from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.models import User
from src.database import get_async_session
from src.auth.base_config import current_user
from src.func import Core

router = APIRouter(
    prefix="/driver",
    tags=["driver"]
)

@router.post("/reg_auto")
async def reg_auto(car_brand, car_model, car_color, car_plate, car_type, num_seats,
                   user: User = Depends(current_user)):
    try:
        car_id = user.id
        await Core.reg_car(car_id, car_brand, car_model, car_color, car_plate, car_type, num_seats)
        return {"message": "Car registration"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/reg")
async def get_driver(car_owner, car_owner_contact, city, license_num,
                     user: User = Depends(current_user), db: AsyncSession = Depends(get_async_session)):
    try:
        id = user.id
        await Core.create_driver(id, license_num, id, car_owner, car_owner_contact, city)
        return {"message": "Driver registration"}
    except Exception as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/change_activity")
async def toggle_user_active(user: User = Depends(current_user), db: AsyncSession = Depends(get_async_session)):
    try:
        await Core.toggle_user_attribute(user, "is_active")

        return user.is_active

    except Exception as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail=str(e))


# @router.get("/set_city")
# async def set_city_driver(user: User = Depends(current_user), db: AsyncSession = Depends(get_async_session), city: str = None):
#     try:
#
#         await Core.change_value(user, 'city', city)
#
#         return user.city
#

