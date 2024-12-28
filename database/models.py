from sqlalchemy import Column, Integer, String, BigInteger, ARRAY, JSON, Boolean
from database import Base
from dataclasses import dataclass


@dataclass
class Titles(Base):
    __tablename__ = "titles"

    id = Column(BigInteger, primary_key=True, nullable=False)
    name = Column(String(300), nullable=False)
    full_name = Column(String(300))
    mal_link = Column(String(300))
    hashtags_all = Column(ARRAY(String))
    hashtags_title = Column(ARRAY(String))
    raw_json = Column(JSON)
    visible = Column(Boolean)
    series_count = Column(Integer)
