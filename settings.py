import config

class Settings:
    def __init__(self, db_host: str, db_port: str, db_user: str, db_pass: str, api_graphhopper: str, secret_auth: str) -> None:
        self.DB_HOST = db_host
        self.DB_PORT = db_port
        self.DB_USER = db_user
        self.DB_PASS = db_pass
        self.API_GRAPHHOPPER = api_graphhopper
        self.SECRET_AUTH = secret_auth


settings = Settings(
    db_host=config.DB_HOST,
    db_port=config.DB_PORT,
    db_user=config.DB_USER,
    db_pass=config.DB_PASS,
    api_graphhopper=config.API_GRAPHHOPPER,
    secret_auth=config.SECRET_AUTH
)