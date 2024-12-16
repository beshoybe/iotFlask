
from database.database import db

from datetime import datetime

class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rate = db.Column(db.String(120), unique=False, nullable=True, default="0")
    quantity = db.Column(db.String(120), unique=False, nullable=True, default="0")
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now())
    connected = db.Column(db.Boolean, default=False)
    def __repr__(self):
        return f'<Device {self.name}>'
    def update(self, rate, quantity):
        self.updated_at = datetime.now()
        self.rate = rate
        self.quantity = quantity
        db.session.commit()
    def update_connection(self, value):
        self.updated_at = datetime.now()
        self.connected = value
        db.session.commit()