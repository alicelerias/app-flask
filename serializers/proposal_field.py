from marshmallow import fields, validate

from .marshmallow import ma
from models.proposal_field import ProposalField


class ProposalFieldSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ProposalField
        load_instance = True

    name = fields.String(required=True, validate=validate.Length(max=20))
    type = fields.String(required=True, validate=validate.OneOf(["string", "integer"]))
    nullable = fields.Boolean(required=True)
    order = fields.Float(required=True)
