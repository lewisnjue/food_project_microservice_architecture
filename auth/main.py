from fastapi import FastAPI, Request
from sqlmodel import Session,SQLModel
from users import engine 
from users import model 
from users._signup_schema import sign_up
from users._handle_signup import handle_signup
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


@app.post("/signup")
async def _signup(request: Request,data:sign_up):
    message, err = handle_signup(data,DB_SESSION)
    if message:
        return{"message":message}
    else:
        return {"error":err}
    

