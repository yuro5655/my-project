# Imports
from pydantic import BaseModel

# User BAse Schema
class User_base(BaseModel):
    name:str
    password:str
    age:int
    adress:str
    phone:int
# User Schema
class User(User_base):
    id:int
    class Config:
        orm_mode = True
# User Create Schema
class User_create(User_base):
    pass
# User Login Schemas
class UserLoginSchemas(BaseModel):
    name:str
    password:str
