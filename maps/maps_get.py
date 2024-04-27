from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Optional
from enum import Enum, auto

from maps.geo import get_route
from settings import settings

class Category(str, Enum):
    ECONOMY = "economy"
    COMFORT = "comfort"
    BUSINESS = "business"
    PREMIUM = "premium"

class TaxiRide(BaseModel):
    category: Category
    distance: float
    start_location: str
    end_location: str

    def calculate_cost(self) -> float:
        base_price: Dict[Category, float] = {
            Category.ECONOMY: 1,
            Category.COMFORT: 1.1,
            Category.BUSINESS: 1.3,
            Category.PREMIUM: 1.6
        }
        pickup_price: Dict[Category, float] = {
            Category.ECONOMY: 30.0,
            Category.COMFORT: 40.0,
            Category.BUSINESS: 50.0,
            Category.PREMIUM: 60.0
        }
        return pickup_price[self.category] + (base_price[self.category] * 17.5 * self.distance)
router = APIRouter(
    prefix = "/maps",
)

@router.get("/newtrip")
def new_trip(category: Category, start_location: str, end_location: str):
    try:
        distance = get_route(settings.API_GRAPHHOPPER, start_location, end_location)
        print(distance)
        if distance is None:
            raise ValueError("Unable to calculate distance. One or more addresses may be incorrect.")
    except Exception as e:
        raise HTTPException(detail=f"An error occurred while calculating the distance. {e}")

    ride = TaxiRide(
        category=category, 
        distance=distance / 1000,
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