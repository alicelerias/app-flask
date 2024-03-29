from marshmallow import fields, validate, Schema

from models.response import Response


class ResponseSchema(Schema):
    class Meta:
        model = Response
        load_instance = True

    id = fields.Integer(dump_only=True)
    field_name = fields.String(required=True, validate=validate.Length(max=20))
    value = fields.String(allow_none=True)
    proposal_id = fields.Integer(required=True)

    proposal_field = fields.Nested("ProposalFieldSchema", only=["name"])
    proposal = fields.Nested("ProposalSchema", only=["status"])
