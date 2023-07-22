from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from .database import Base
import uuid

class Role(Base):
    __tablename__ = "roles"
    id = Column(String(36), primary_key=True, index=True, nullable=False, default=lambda:str(uuid.uuid4()), unique=True)
    name = Column(String(36))

class User(Base):
    __tablename__ = "users"
    id = Column(String(200), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    firstname = Column(String(50))
    lastname = Column(String(50))
    phone = Column(String(14))
    email = Column(String(50))
    password = Column(String(500))
    userRole = relationship("RoleUser", back_populates="user")

class RoleUser(Base):
    __tablename__ = "role_user"
    id = Column(String(36), primary_key=True, index=True, unique=True, default=lambda:str(uuid.uuid4), nullable=False)
    user_id = Column(String(36), ForeignKey("users.id"))
    role_id = Column(String(36), ForeignKey("roles.id"))
    user = relationship("User", back_populates="userRole")

class Clinic_Category(Base):
    __tablename__ = "clinic_categories"
    id = Column(String(36), primary_key=True, index=True, default=lambda: str(uuid.uuid4(), unique=True, nullable=False))
    name = Column(String(50), index=True)
    description = Column(String(500), nullable=True)

    clinic_category = relationship("Clinic", back_populates="category")

class Country(Base):
    __tablename__ = "countries"
    id = Column(String(36), primary_key=True, nullable=False, index=True, default=lambda: str(uuid.uuid4()), unique=True)
    name = Column(String(36))
    code = Column(String(10))

class Region(Base):
    __tablename__ = "regions"
    id = Column(String(36), primary_key=True, index=True, nullable=False, default=lambda: str(uuid.uuid4()), unique=True)
    name = Column(String(50))
    code = Column(String(50))
    country_id = Column(String(36), ForeignKey("countries.id"))

class District(Base):
    __tablename__ = "districts"
    id = Column(String(36), primary_key=True, index=True, nullable=False, default=lambda: str(uuid.uuid4()), unique=True)
    name = Column(String(50))
    district_id = Column(String(36), ForeignKey("regions.id"), index=True)

class Ward(Base):
    __tablename__ = "wards"
    id = Column(String(36), primary_key=True, index=True, nullable=False, default=lambda: str(uuid.uuid4()), unique=True)
    name = Column(String(50))
    district_id = Column(String(36), ForeignKey("districts.id"))

class Clinic(Base):
    __tablename__ = "clinics"
    id = Column(String(36), primary_key=True, index=True, nullable=False, default=lambda: str(uuid.uuid4()), unique=True)
    name = Column(String(50))
    clinic_phone = Column(String(14))
    clinic_email = Column(String(50))
    ward_id = Column(String(36), ForeignKey("wards.id"))
    category_id = Column(String(36), ForeignKey("clinic_categories.id"))

    category = relationship("Clinic_Category", back_populates="clinic_category")