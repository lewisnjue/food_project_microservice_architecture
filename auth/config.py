from pydantic_settings import BaseSettings
from pathlib import Path 
from functools import lru_cache 

class settings(BaseSettings):
    secret_key: str 
    algorithm: str 
    exp: int 

    class Config:
        env_file = '.env'


@lru_cache
def get_settings():
    """
    return the settings of the application 
"""
    return settings() #noqa
