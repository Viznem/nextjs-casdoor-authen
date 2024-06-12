from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name :str = "App API"
    
    class Config:
        env_prefix = ".env"
        