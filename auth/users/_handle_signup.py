from .model import Users
from sqlmodel import select 
from .security import hash_password


def handle_signup(data,DB_SESSION):
    email = data.email
    password = data.password
    statement  = select(Users).where(Users.email == email)
    q = DB_SESSION.exec(statement)
    q = list(q)
    if len(q) == 1:
        return None,"email not availabe"
    else:
        _hashed = hash_password(password)
        obj = Users(email=email,password=str(_hashed))
        DB_SESSION.add(obj)
        DB_SESSION.commit()
        return "user created", None

