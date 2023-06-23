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
        return jsonify({'errors': error.messages}), 400
    proposal_field = ProposalField(**proposal_field_data)

    db.session.add(proposal_field)
    db.session.commit()

    response = serializer.dump(proposal_field)
    return jsonify(response), 201

@proposal_field_bp.route('/proposal_fields', methods=["GET"])
def get_proposal_fields():
    serializer = ProposalFieldSchema(many=True)
    proposal_fields = ProposalField.query.all()
    response = serializer.dump(proposal_fields)
    return jsonify(response), 200


@proposal_field_bp.route('/proposal_fields/<field_name>', methods=["POST"])
def update_proposal_field(field_name):
    proposal_field = ProposalField.query.filter_by(name=field_name).first()
    if not proposal_field:
        return jsonify({'error': 'Proposal field not found'}), 404
    proposal_field_data = request.json
    for key, value in proposal_field_data.items():
        setattr(proposal_field, key, value)
    db.session.commit()
    response = serializer.dump(proposal_field)
    return jsonify(response), 200

@proposal_field_bp.route('/proposal_fields/<field_name>', methods=["DELETE"])
def delete_proposal_field(field_name):
    proposal_field = ProposalField.query.filter_by(name=field_name).first()
    if not proposal_field:
        return jsonify({'error': 'Proposal field not found'}), 404
    db.session.delete(proposal_field)
    db.session.commit()
    return jsonify({"message": "proposal field deleted sucessfully"}), 200

    


    
       