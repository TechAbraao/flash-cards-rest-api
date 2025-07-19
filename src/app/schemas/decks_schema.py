from marshmallow import Schema, fields

class RequestDecksSchema(Schema):
    title = fields.Str()
    description = fields.Str()
    tags = fields.List(fields.Str())
    
request_decks_schema = RequestDecksSchema()

class RequestDeckIdSchema(Schema):
    id = fields.UUID(required=True)
    
request_deck_id_schema = RequestDeckIdSchema()