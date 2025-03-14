from pydantic import BaseModel 
from pydantic import EmailStr 


class _token(BaseModel):
    email:  EmailStr
    password: str 





