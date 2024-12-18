from pydantic import BaseSettings

# Check and validate that all env variables are available
class Settings(BaseSettings):
    # PostgreSQL DB
    db_username: str
    db_password: str
    db_hostname: str
    db_port: str
    db_name: str
    
    # JWT
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int = 30

    class Config:
        env_file = ".env"

settings = Settings()