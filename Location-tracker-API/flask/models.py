from state import db
from datetime import datetime
class Location(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.String(80))
    latitude=db.Column(db.Float)
    longitude=db.Column(db.Float)
    timestamp=db.Column(db.DateTime,default=datetime.utcnow)
