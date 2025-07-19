
from marshmallow import Schema, fields

class RequestCardSchema(Schema):
    question = fields.Str(required=True)
    answer = fields.Str(required=True)
    tags = fields.List(fields.Str(required=True))