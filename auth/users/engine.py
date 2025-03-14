from sqlmodel import create_engine



def _engine():
    """
    create an engine with my database and retun the engine 
    """
    db_name = "database.db"
    db_url = f"sqlite:///{db_name}"
    engine = create_engine(db_url,echo=True)
    return engine 

