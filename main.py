from fastapi import FastAPI, Depends, Response, status, HTTPException
from typing import List
from datetime import datetime
from sql_db import schemas, models
from sqlalchemy.orm import Session
import bcrypt

from sql_db.database import engine, SessionLocal


app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def index():
    return {"data": {"name": "Sharifu", "email": "sharifumasudi66@gmail.com", "created_at": datetime.now()}}

@app.post("/user", tags=["users"], status_code=status.HTTP_200_OK, response_model=schemas.AddUser)
async def create(request: schemas.AddUser, db: Session = Depends(get_db)):
    salt = bcrypt.gensalt()
    new_user = models.User(
        firstname=request.firstname,
        lastname=request.lastname,
        phone=request.phone,
        email=request.email,
        password=bcrypt.hashpw(request.password.encode("utf-8"), salt)
        )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Get users
@app.get("/users",status_code=status.HTTP_200_OK,response_model=List[schemas.ShowUser], tags=["users"])
async def getUsers(db: Session = Depends(get_db)):
    userList = db.query(models.User).outerjoin(models.RoleUser, models.User.id==models.RoleUser.user_id).all()
    if not userList:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No user until now!")
    return userList

# Get single user
@app.get("/users/{id}", status_code=200, tags=["users"])
async def getUser(id: str, response: Response, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"requested user with id {id} notfound")
    return {"data": user}

# Delete user
@app.delete("/user/{id}", tags=["users"])
async def delete(id: str, db: Session = Depends(get_db)):
    db.query(models.User).filter(models.User.id == id).delete(synchronize_session=False)
    db.commit()
    return {"user with id": f"{id} Deleted!"}

# update user
@app.put("/user/{id}", status_code=status.HTTP_202_ACCEPTED, tags=["users"])
async def update_user(id: str, request: schemas.User, db: Session = Depends(get_db)):
    # Get the user from the database
    user = db.query(models.User).filter(models.User.id == id).first()

    if user:
        # Update the user fields based on the request
        user.firstname = request.firstname
        user.lastname = request.lastname
        user.phone = request.phone
        user.email = request.email
        user.password = request.password

        # Commit the changes to the database
        db.commit()

        return {"Data": f"User with {id} successfully updated"}
    else:
        return {"Data": f"User with {id} not found"}

# Store role
@app.post("/roles", status_code=status.HTTP_202_ACCEPTED, tags=['Roles'])
async def createRole(request: schemas.showRoles, db: Session=Depends(get_db)):
    role = models.Role(name=request.name)
    db.add(role)
    db.commit()
    db.refresh(role)
    return {"data": role}

# Get roles
@app.get("/roles", status_code=status.HTTP_200_OK, response_model=List[schemas.showRoles], tags=["Roles"])
async def getRoles(db: Session=Depends(get_db)):
    roles = db.query(models.Role).all()
    if not roles:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No roles available")
    return roles

