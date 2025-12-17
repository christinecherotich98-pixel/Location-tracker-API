from flask import Blueprint,request,jsonify
from models import Location
from state import db
from sqlalchemy import func
bp=Blueprint('bp',__name__)

@bp.route('/locations',methods=['POST'])
def add():
    l=Location(**request.json)
    db.session.add(l); db.session.commit()
    return jsonify(status='stored'),201

@bp.route('/locations')
def latest():
    sub=db.session.query(Location.user_id,func.max(Location.timestamp).label('t')).group_by(Location.user_id).subquery()
    q=db.session.query(Location).join(sub,(Location.user_id==sub.c.user_id)&(Location.timestamp==sub.c.t))
    return jsonify([{'user_id':x.user_id,'latitude':x.latitude,'longitude':x.longitude,'timestamp':x.timestamp.isoformat()} for x in q])

@bp.route('/locations/<user_id>')
def one(user_id):
    l=Location.query.filter_by(user_id=user_id).order_by(Location.timestamp.desc()).first()
    return jsonify({'user_id':l.user_id,'latitude':l.latitude,'longitude':l.longitude,'timestamp':l.timestamp.isoformat()}) if l else ({},404)

@bp.route('/locations/<user_id>/history')
def hist(user_id):
    return jsonify([{'user_id':x.user_id,'latitude':x.latitude,'longitude':x.longitude,'timestamp':x.timestamp.isoformat()} for x in Location.query.filter_by(user_id=user_id).all()])
