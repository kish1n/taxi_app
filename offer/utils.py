import requests
from enum import Enum
from typing import Dict
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from pydantic import BaseModel

geolocator = Nominatim(user_agent="taxi_app_kh_1488")

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


def get_latitude_longitude(address: str):

    try:
        location = geolocator.geocode(address)
        print(location.address)
        if location:
            return location.latitude, location.longitude
        else:
            return None, None
    except GeocoderTimedOut:
        return get_latitude_longitude(address)

def get_route(api_key: str, start_address: str, end_address: str):
    start_lat, start_lon = get_latitude_longitude(start_address)
    end_lat, end_lon = get_latitude_longitude(end_address)
    url = f"https://graphhopper.com/api/1/route?point={start_lat},{start_lon}&point={end_lat},{end_lon}&vehicle=car&locale=en&key={api_key}"
    response = requests.get(url)
    data = response.json()
    return data['paths'][0]['distance'] / 1000  # Расстояние в метрах
