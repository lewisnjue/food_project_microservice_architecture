from pydantic import BaseModel 
from pydantic import EmailStr 


class sign_up(BaseModel):
    email:  EmailStr
    password: str 

