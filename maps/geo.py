import requests
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

geolocator = Nominatim(user_agent="taxi_app_kh_1488")

def get_latitude_longitude(address: str):

    try:
        location = geolocator.geocode(address)
        print(location.address)
        if location:
            return (location.latitude, location.longitude)
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
    return data['paths'][0]['distance']  # Расстояние в метрах

