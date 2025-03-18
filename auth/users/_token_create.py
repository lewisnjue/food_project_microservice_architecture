import jwt
import datetime
import uuid

def create_access_token(data: dict, secret_key: str, algorithm: str, expires_delta):
    to_encode = data.copy()

    if "id" in to_encode and isinstance(to_encode["id"], uuid.UUID):
        to_encode["id"] = str(to_encode["id"])

    if expires_delta:
        expire = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=expires_delta)
    else:
        expire = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=15)

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, secret_key, algorithm=algorithm)

    return encoded_jwt, None

