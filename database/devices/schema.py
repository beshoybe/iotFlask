from marshmallow_sqlalchemy import SQLAlchemySchema
from marshmallow import fields 
from database.database import db
from database.devices.model import Device

class DeviceSchema(SQLAlchemySchema):
    class Meta:
        model = Device
        sqla_session = db.session
    id = fields.Int(dump_only=True)
    rate = fields.String()
    quantity = fields.String()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
 