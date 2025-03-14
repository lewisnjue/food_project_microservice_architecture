import bcrypt

def hash_password(raw_password: str):
    """
    Takes a raw password, encodes it,
    hashes the password, and returns the hashed password as a string.
    """
    _password = raw_password.encode("utf-8")
    _hashed_password = bcrypt.hashpw(_password, bcrypt.gensalt())
    _hashed_password = _hashed_password.decode('utf-8')  # Stored as string (DB friendly)
    return _hashed_password

def verify_password(raw_password: str, hashed: str):
    """
    Verifies a raw password against a hashed password.
    """
    _password = raw_password.encode("utf-8")
    _hashed = hashed.encode("utf-8")  # Convert string back to bytes
    return bcrypt.checkpw(_password, _hashed)

