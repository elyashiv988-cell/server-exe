from fastapi import HTTPException
from hashing import verify_password
from models import Creds



def authenticate(creds: Creds, data_users, allowed_types: list[str]):
    for user in data_users:
        if creds.username == user["username"] and verify_password(creds.password, user["password"]):
            if user["type"] not in allowed_types:
                raise HTTPException(status_code=401, detail="Not enough permissions")
            return user
    raise HTTPException(status_code=403, detail="Incorrect login details")