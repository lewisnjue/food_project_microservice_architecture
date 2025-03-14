from fastapi import FastAPI, Request
from sqlalchemy.engine import create
from sqlmodel import Session,SQLModel
from users import engine 
from users.token_schema import _token
from users import model 
from users._signup_schema import sign_up
from users._handle_signup import handle_signup
from users._token_create import create_access_token
from users.query import check_user
from config import get_settings
db_engine = engine._engine() 

settings =  get_settings()


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
    
@app.post("/token")
async def _token(request:Request,data:_token):
    _data  = data
    id, err = check_user(db_session=DB_SESSION,email=_data.email,raw_password=_data.password)
    if err:
        return {"error":err}
    
    

    token, err  = create_access_token(id,settings.secret_key,settings.algorithm,settings.exp)
    if err:
        return {"error":err}
    else:
        return token 
    

