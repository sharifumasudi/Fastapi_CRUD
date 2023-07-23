from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session
from app import models, schemas, database
from ..sql import role
from typing import List

router = APIRouter(
    prefix="/api/v1/role",
    tags=['Roles']
)
    
# Get roles
@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.showRoles])
async def getRoles(db: Session=Depends(database.get_db)):
  return role.get(db)

# Store role
@router.post("/", status_code=status.HTTP_202_ACCEPTED)
async def createRole(request: schemas.showRoles, db: Session=Depends(database.get_db)):
   return role.create(request, db)

