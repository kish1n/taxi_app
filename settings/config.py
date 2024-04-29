from dotenv import load_dotenv

import os

load_dotenv()

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")

API_GRAPHHOPPER = os.environ.get("API_GRAPHHOPPER")

SECRET_AUTH = os.environ.get("SECRET_AUTH")

class Settings:
    def __init__(self, db_host: str, db_port: str, db_user: str, db_pass: str, db_name: str, api_graphhopper: str, secret_auth: str) -> None:
        self.DB_HOST = db_host
        self.DB_PORT = db_port
        self.DB_USER = db_user
        self.DB_PASS = db_pass
        self.DB_NAME = db_name
        self.API_GRAPHHOPPER = api_graphhopper
        self.SECRET_AUTH = secret_auth

settings = Settings(
    db_host=DB_HOST,
    db_port=DB_PORT,
    db_user=DB_USER,
    db_pass=DB_PASS,
    db_name=DB_NAME,
    api_graphhopper=API_GRAPHHOPPER,
    secret_auth=SECRET_AUTH
)