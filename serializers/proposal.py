from marshmallow import fields, validate, Schema

from models.proposal import Proposal

class ProposalSchema(Schema):
    class Meta:
        model = Proposal
        load_instance = True

    id = fields.Integer(dump_only=True)
    status = fields.String(required=True, validate=validate.OneOf(["pending", "approved", "denied"]))
