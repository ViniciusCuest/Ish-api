from api import ma
from marshmallow import Schema, fields

class UserSchema(ma.Schema):
    class Meta:
        fields = ("_id", "full_name", "birth", "identifier", "work_authorization_code", "phone", "email", "password")
        
    _id = fields.Str()
    full_name = fields.Str(required=True)
    birth = fields.Str(required=True)
    identifier = fields.Str(required=True)
    work_authorization_code = fields.Str(required=False)
    phone= fields.Str(required=True)
    email= fields.Str(required=True)
    password= fields.Str(required=True)
    