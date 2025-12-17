from sqlalchemy import Column,Integer,String,Float,DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
Base = declarative_base()
class Location(Base):
    __tablename__="locations"
    id=Column(Integer,primary_key=True)
    user_id=Column(String)
    latitude=Column(Float)
    longitude=Column(Float)
    timestamp=Column(DateTime,default=datetime.utcnow)
