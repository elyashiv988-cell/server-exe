from pydantic import BaseModel

class Creds(BaseModel):
    username: str
    password: str