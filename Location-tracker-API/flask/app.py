from flask import Flask
from state import db
from routes import bp
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///locations.db'
db.init_app(app)
app.register_blueprint(bp)
with app.app_context(): db.create_all()
if __name__=='__main__': app.run(host='0.0.0.0',port=5000)
