# Imports
from fastapi import FastAPI, Response, Depends, HTTPException, UploadFile
from fastapi.responses import StreamingResponse , FileResponse
from sqlalchemy.orm import Session
from authx import AuthX, AuthXConfig
from databaze import session_local, engine
from models import base, User_Model
from schemas import User, User_create, UserLoginSchemas
from typing import List
# Create Appi
app = FastAPI()
# Create tags
tags_all=["My_first_Project"]
# Create token and cookies
config = AuthXConfig()
#accses cookie name
config.JWT_ACCESS_COOKIE_NAME = "my_token"
# Secret key
config.JWT_SECRET_KEY = "Yuro5655"
# Accses token locaton
config.JWT_TOKEN_LOCATION = ["cookies"]

security = AuthX(config=config)
# Create database
base.metadata.create_all(bind= engine)

def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()
# Registred User
@app.post("/registred",summary="registr", response_model=User_create, tags=tags_all)
async def register(creds: User_create, db: Session = Depends(get_db)):
    db_user = User_Model(
        name=creds.name,
        password=creds.password,
        age=creds.age,
        adress=creds.adress,
        phone=creds.phone
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.post("/login", summary="login", tags=tags_all)
async def login(creds: UserLoginSchemas, response: Response, db: Session = Depends(get_db)):
    # Find user by name
    db_user = db.query(User_Model).filter(User_Model.name == creds.name).first()
    
    if not db_user or db_user.password != creds.password:
        raise HTTPException(status_code=401, detail="Incorrect username or password")

    # Create a token with user ID

    token = security.create_access_token(uid=str(db_user.id))
    response.set_cookie(config.JWT_ACCESS_COOKIE_NAME, token)

    return {"access_token": token}
# User Delete
@app.delete("/delete/{user_id}",summary="delete user",tags=tags_all, dependencies=[Depends(security.access_token_required)])
async def delete(user_id:int,db: Session = Depends (get_db)):
    user = db.query(User_Model).filter(User_Model.id == user_id).first()

    if not user:
         raise HTTPException(status_code=404, detail="User not faund")

    db.delete(user)
    db.commit()
    return("user delete")
# Find user by Id
@app.get("/user/{user_id}", summary=" user id",tags=tags_all, dependencies=[Depends(security.access_token_required)])
async def Delete_user(user_id:int, db: Session = Depends (get_db)):
     # Find user by Id
    user = db.query(User_Model).filter(User_Model.id == user_id).first()

    if not user:
         raise HTTPException(status_code=404, detail="User not faund")
    
    return(user)
# User List
@app.get("/users_list/", response_model=List[User], tags=tags_all, summary="список users", dependencies=[Depends(security.access_token_required)])
async def user_list(db: Session = Depends(get_db)):
    return db.query(User_Model).all()
# Upload Profil photos
@app.post("/mfiles",tags=tags_all, summary="uploadet files")
async def upload_files(uploaded_files: list[ UploadFile]):
    for uploaded_file in uploaded_files:
        file = uploaded_file.file
        filename =  uploaded_file.filename
        with open(f"1_{filename}", "wb") as f:
            f.write(file.read())
# Get Profil Photos
@app.get("/fileget/{filename}", tags=tags_all, summary="get file")
async def fileget(filename:str):
    return FileResponse(filename)

