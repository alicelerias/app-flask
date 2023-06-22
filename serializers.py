from marshmallow import fields, validate
from flask_marshmallow import Marshmallow

from .models import proposalfield


ma = Marshmallow()


def configure(app):
    ma.init_app(app)


class ClientSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = proposalfield.Client
        load_instance = True

    user_name = fields.Str(required=True, validate=validate.Length(min=6, max=15))
    email = fields.Str(
        required=True, validate=validate.Email(error="Insert a valid email")
    )
    password = fields.Str(required=True, validate=validate.Length(min=6, max=15))
