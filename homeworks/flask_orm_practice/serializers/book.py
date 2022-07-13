from marshmallow import Schema, fields
from marshmallow.validate import Length


class BookSchema(Schema):
    book_id = fields.Integer(required=True, dump_only=True)
    name_book = fields.String(required=True, validate=Length(min=3, max=355))
    author_book = fields.String(required=True, validate=Length(min=3, max=355))