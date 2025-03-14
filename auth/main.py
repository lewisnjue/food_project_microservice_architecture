from fastapi import FastAPI 
from sqlmodel import Session,SQLModel
from users import engine 
from users import model 

db_engine = engine._engine() 




app = FastAPI() 

DB_SESSION = None 
@app.on_event("startup")
def on_startup():

    SQLModel.metadata.create_all(db_engine)

    global DB_SESSION
    DB_SESSION = Session(db_engine)
    


@app.get("/")
async def home():
    return {"hello":"world"}
