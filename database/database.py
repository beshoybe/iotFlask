from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from database.devices.model import *

def init_database(app):
    # app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://coderoen_saraya:elsaraya2024@127.0.0.1:3306/coderoen_elsaraya'
    app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://smartflow:smart1234@db4free.net:3306/smartflow'    
    db.init_app(app)
    with app.app_context():
        db.create_all()
