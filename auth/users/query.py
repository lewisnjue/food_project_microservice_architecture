from sqlmodel import select
from .model import Users
from .security import verify_password

def check_user(db_session, email, raw_password):
    # Build and execute the query
    statement = select(Users).where(Users.email == email)
    q = db_session.exec(statement).first()

    # If no user is found
    if not q:
        return None, "invalid credentials"

    # Verify the password
    hashed_password = q.password
    valid_password = verify_password(raw_password=raw_password, hashed=hashed_password)

    # Return user ID if valid, else error message
    if valid_password:
        return {"id": q.id}, None
    else:
        return None, "invalid credentials"

