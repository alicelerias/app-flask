from flask import Blueprint, jsonify, request
from marshmallow import ValidationError

from serializers.proposal_field import ProposalFieldSchema
from models.proposal_field import ProposalField
from db.alchemy import get_db

proposal_field_bp = Blueprint("proposal_field", __name__)

db = get_db()
serializer = ProposalFieldSchema()

@proposal_field_bp.route('/proposal_fields', methods=["POST"])
def create_proposal_field():
    data = request.json
    try:
        proposal_field_data = serializer.load(data)
    except ValidationError as error:
        return jsonify({'errors': error.messages}, 400)
    proposal_field = ProposalField(**proposal_field_data)

    db.session.add(proposal_field)
    db.session.commit()

    response = serializer.dump(proposal_field)
    response = serializer.dump(proposal_field)
    return jsonify(response), 201
