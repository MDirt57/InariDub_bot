from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise "DATABASE_URL not found"

engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)
Base = declarative_base()


