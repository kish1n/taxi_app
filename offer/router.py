from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import Dict
from enum import Enum

from offer.utils import get_route
from config import settings
from offer.utils import Category, TaxiRide

from auth.models import User, metadata
from auth.base_config import current_user

router = APIRouter(
    prefix="/offer",
    tags=["offer"]
)

@router.get("/newtrip")
async def new_trip(
        category: Category,
        start_location: str,
        end_location: str,
        user: User = Depends(current_user)
):
    try:
        distance = get_route(settings.API_GRAPHHOPPER, start_location, end_location)
        print(distance)
        if distance is None:
            raise ValueError("Unable to calculate distance. One or more addresses may be incorrect.")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"An error occurred while calculating the distance. {e}")

    ride = TaxiRide(
        category=category,
        distance=distance,
        start_location=start_location,
        end_location=end_location
    )

    return {
        "category": ride.category,
        "distance": ride.distance,
        "start_location": ride.start_location,
        "end_location": ride.end_location,
        "cost": ride.calculate_cost()
    }

