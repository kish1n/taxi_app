from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import Dict
from enum import Enum

from src.offer.utils import get_route
from src.config import settings
from src.offer.utils import Category, TaxiRide

from src.auth.models import User, metadata
from src.auth.base_config import current_user

router = APIRouter(
    prefix="/offer",
    tags=["offer"]
)

@router.get("/trip")
async def new_trip(
        category: Category,
        start_location: str,
        end_location: str,
        user: User = Depends(current_user)
):
    try:
        distance = get_route(settings.API_GRAPHHOPPER, start_location, end_location)
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

    message = {
        "message": f"New trip ordered from {start_location} to {end_location}",
        "category": category.name,
        "distance": distance,
        "cost": ride.calculate_cost()
    }

    print(message)

    return {
        "category": ride.category,
        "distance": ride.distance,
        "start_location": ride.start_location,
        "end_location": ride.end_location,
        "cost": ride.calculate_cost()
    }

