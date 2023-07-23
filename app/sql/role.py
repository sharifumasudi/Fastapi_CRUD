from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app import models

def get(db: Session):
    roles = db.query(models.Role).all()
    if not roles:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No roles available")
    return roles

def create(request, db: Session):
    role = models.Role(name=request.name)
    db.add(role)
    db.commit()
    db.refresh(role)
    return {"data": role}

