from sqlmodel import create_engine
from config import get_settings


settings = get_settings() 


def _engine():
    """
    create an engine with my database and retun the engine 
    """
    db_url = settings.db_url
    engine = create_engine(db_url,echo=True)
    return engine 

