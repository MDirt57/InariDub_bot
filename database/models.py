from sqlalchemy import Column, Integer, String, BigInteger, ARRAY, JSON, Boolean, SmallInteger
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

@dataclass
class Series(Base):
    __tablename__ = "series"

    id = Column(BigInteger, primary_key=True, nullable=False)
    type = Column(Boolean, nullable=False)
    msg_id = Column(Integer, nullable=False)
    video_id = Column(BigInteger, nullable=False)
    raw_json = Column(JSON)
    name = Column(String(200))
    description = Column(String(255))
    title_id = Column(BigInteger)
    source_message_id = Column(BigInteger)
    episode_number = Column(SmallInteger)
    bot_json = Column(JSON)
    bot_video_id = Column(String(255))