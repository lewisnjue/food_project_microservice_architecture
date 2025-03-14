from fastapi import HTTPException, status
import jwt



def  validate_token(token, secret_key, algorithm,*args,**kwargs):
    credentials_exception = HTTPException(
                status_code = status.HTTP_401_UNAUTHORIZED,
                detail ="could not validate credentials",
                headers={"WWW-Authenticate":"Bearer"}
                )
    try:
        payload = jwt.decode(token,secret_key,algorithms=[algorithm])

        id = payload.get("id")
        if id is None:
            raise credentials_exception
    except jwt.InvalidTokenError:
            raise credentials_exception
        
    if id is None:
            raise credentials_exception
        

    return id 



