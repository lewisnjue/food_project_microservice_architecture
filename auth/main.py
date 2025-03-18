from fastapi import Depends, FastAPI, Request,HTTPException,status
from sqlalchemy.engine import create
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import raiseload, session
from sqlmodel import Session,SQLModel, except_
from users import engine 
from users.token_schema import _token
from users import model 
from users._signup_schema import sign_up
from users._handle_signup import handle_signup
from users._token_create import create_access_token
from users.query import check_user
from config import get_settings
from users.validators import validate_token
from contextlib import contextmanager # this is for yielding session 
db_engine = engine._engine() 

settings =  get_settings()


app = FastAPI() 


def get_db_session():
    with Session(db_engine) as session:
        try:
            yield session
            session.commit()
        except SQLAlchemyError as e:
            session.rollback() 
            print(f"session rollback because of error: {e}")
            raise 
        finally:
            session.close() 



@app.on_event("startup")
def on_startup():

    SQLModel.metadata.create_all(db_engine)

    

@app.get("/")
async def home():
    return {"hello":"world"}


@app.post("/signup")
async def _signup(request: Request,data:sign_up,session:Session = Depends(get_db_session)):
    message, err = handle_signup(data,session)
    if message:
        return{"message":message}
    else:
        return {"error":err}

@app.post("/token")
async def _token(request:Request,data:_token,session:Session = Depends(get_db_session)):
    _data  = data
    id, err = check_user(db_session=session,email=_data.email,raw_password=_data.password)
    if err:
        return {"error":err}
    
    

    token, err  = create_access_token(id,settings.secret_key,settings.algorithm,settings.exp)
    if err:
        return {"error":err}
    else:
        return token 
    

@app.post("/validate")
async def _validate_token(request: Request):
    auth_header = request.headers.get("Authorization")

    if not auth_header:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authorization header missing",
            headers={"WWW-Authenticate": "Bearer"},
        )

    parts = auth_header.split(" ")
    if len(parts) != 2 or parts[0].lower() != "bearer":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authorization header format. Expected 'Bearer <token>'.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    token = parts[1]
    id = validate_token(token,settings.secret_key,settings.algorithm)
    return True 
    

