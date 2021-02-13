from pydantic import BaseModel
class Users(BaseModel):
    user_id:int
    name:str
    age:int