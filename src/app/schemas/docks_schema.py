from marshmallow import Schema, fields

class RequestDecksSchema(Schema):
    title = fields.Str()
    description = fields.Str()
    tags = fields.List(fields.Str())
    
request_decks_schema = RequestDecksSchema()