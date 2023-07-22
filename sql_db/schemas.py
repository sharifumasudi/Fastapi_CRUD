from pydantic import BaseModel, EmailStr
from typing import Optional

class Role(BaseModel):
    id: str
    name: str
class showRoles(BaseModel):
    name: str

class User(BaseModel):
    id: Optional[str] = None
    firstname: str
    lastname: str
    phone: str
    email : EmailStr
    password: str

class AddUser(BaseModel):
    firstname: str
    lastname: str
    phone: str
    email : EmailStr
    password: str

    class Config():
        orm_mode = True

class ShowUser(BaseModel):
    firstname: str
    lastname: str
    phone: str
    email : str

    class Config():
        orm_mode = True

class RoleUser(BaseModel):
    user_id: str
    role_id: str

class Clinic_Category(BaseModel):
    id: str
    name: str
    description: Optional[str] = None

class Country(BaseModel):
    id: str
    name: str
    code: str

class Region(BaseModel):
    id: str
    name: str
    code: str
    country_id: str

class District(BaseModel):
    id: str
    name: str
    regional_id: str

class Ward(BaseModel):
    id: str
    name: str
    district_id: str

class Clinic(BaseModel):
    id: str
    name: str
    clinic_phone: str
    clinic_email: str
    ward_id: str
    clinic_Category_id: str