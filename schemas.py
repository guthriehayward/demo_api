from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int() 
    username = fields.Str()
    password = fields.Str()
    email = fields.Email()
    created_at = fields.DateTime()