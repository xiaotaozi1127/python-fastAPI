from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Default App"
    debug: bool = False
    port: int = 8000

    class Config:
        env_file = ".env"

settings = Settings()
