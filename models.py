# Imports
from sqlalchemy import Column, Integer, String, ForeignKey, BigInteger
from sqlalchemy.orm import relationship
from databaze import base

# User Model
class User_Model(base):

    __tablename__ = "Users"
    
    id = Column(Integer, index=True, primary_key=True, autoincrement=True)
    age = Column(Integer)
    name = Column(String)
    password = Column(String,)
    adress = Column(String)
    phone = Column(BigInteger)