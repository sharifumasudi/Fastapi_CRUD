from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from app import schemas, database
from typing import List
from ..sql import user

router = APIRouter(
    prefix="/api/v1/user",
    tags=['Users']
)
    
    # Get users
@router.get("/",status_code=status.HTTP_200_OK,response_model=List[schemas.ShowUser])
async def getUsers(db: Session = Depends(database.get_db)):
    return user.get(db)

# Get single user
@router.get("/{id}", status_code=200)
async def getUser(id: str, db: Session = Depends(database.get_db)):
    return user.show(id, db)
    

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.AddUser)
async def create(request: schemas.AddUser, db: Session = Depends(database.get_db)):
    return user.create(request, db)

# # update user
@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_user(id: str, request: schemas.UpdateUser, db: Session = Depends(database.get_db)):
    return user.update(id, request, db)

# # Delete user
@router.delete("/{id}")
async def delete(id: str, db: Session = Depends(database.get_db)):
    return user.destroy(id, db)