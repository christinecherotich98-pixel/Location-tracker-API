from fastapi import APIRouter
from models import Location,Base
from state import engine,SessionLocal
from datetime import datetime
from sqlalchemy import func
router=APIRouter()
Base.metadata.create_all(bind=engine)

@router.post("/locations",status_code=201)
def add(loc:dict):
    db=SessionLocal()
    l=Location(**loc,timestamp=datetime.utcnow())
    db.add(l); db.commit()
    return {"status":"stored"}

@router.get("/locations")
def latest():
    db=SessionLocal()
    sub=db.query(Location.user_id,func.max(Location.timestamp).label("t")).group_by(Location.user_id).subquery()
    return db.query(Location).join(sub,(Location.user_id==sub.c.user_id)&(Location.timestamp==sub.c.t)).all()

@router.get("/locations/{user_id}")
def one(user_id:str):
    db=SessionLocal()
    return db.query(Location).filter_by(user_id=user_id).order_by(Location.timestamp.desc()).first()

@router.get("/locations/{user_id}/history")
def history(user_id:str):
    db=SessionLocal()
    return db.query(Location).filter_by(user_id=user_id).order_by(Location.timestamp).all()
