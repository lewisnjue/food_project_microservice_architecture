import bcrypt 






def hash_password(raw_password:str):
    """
    this function takes a raw password and encode it 
    then hash the  password and return hashed password 
    """
    _password = raw_password.encode("utf-8")
    _hashed_password = bcrypt.hashpw(_password,bcrypt.gensalt())
    _hashed_password = _hashed_password.decode('utf-8')

    return _hashed_password 



def verify_password(raw_password:str,hashed):
    _password = raw_password.encode("utf-8")
    if bcrypt.checkpw(_password,hashed):
        return True 
    else:
        return False 

