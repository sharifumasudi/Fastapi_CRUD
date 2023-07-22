from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from databases import Database
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+pymysql://shahama:Masoudcodes!1234$2023@localhost:3306/fastapi"

database = Database(DATABASE_URL)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()