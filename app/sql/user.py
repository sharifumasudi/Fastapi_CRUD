from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app import models
import bcrypt


def get(db: Session):
    userList = db.query(models.User).outerjoin(models.RoleUser, models.User.id==models.RoleUser.user_id).all()
    if not userList:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No user until now!")
    return userList

def show(id: str, db):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"requested user with id {id} notfound")
    return {"data": user}

def create(request, db):
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

def update(id: str, request, db: Session):
        # Get the user from the database
    user = db.query(models.User).filter(models.User.id == id).first()

    if user:
        # Update the user fields based on the request
        user.firstname = request.firstname
        user.lastname = request.lastname
        user.phone = request.phone
        user.email = request.email
        # Commit the changes to the database
        db.commit()

        return {"Data": f"User with {id} successfully updated"}
    else:
        return {"Data": f"User with {id} not found"}

def destroy(id: str, db: Session):
        user = db.query(models.User).filter(models.User.id == id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user of ID: {id} not found! process cancelled")
        db.query(models.User).filter(models.User.id == id).delete(synchronize_session=False)
        db.commit()
        return {"user with id": f"{id} Deleted!"}
