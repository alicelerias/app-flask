from flask import Blueprint, jsonify, request
from marshmallow import ValidationError

from serializers.response import ResponseSchema
from serializers.proposal import ProposalSchema
from models.response import Response
from models.proposal import Proposal
from db.alchemy import get_db
from tasks import process_proposal

response_bp = Blueprint("response", __name__)

db = get_db()
response_serializer = ResponseSchema()
proposal_serializer = ProposalSchema()

@response_bp.route('/proposal', methods=["POST"])
def create_response():
    try:
        proposal = {
            "status": "pending"
        }
        proposal_data = proposal_serializer.load(proposal)
        proposal_model = Proposal(**proposal_data)

        with db.session.begin():
            try:
                db.session.add(proposal_model)
                db.session.flush()

                data = request.json.get("responses", [])
                response_models = []

                for response in data:
                    response["proposal_id"] = proposal_model.id
                    response_data = response_serializer.load(response)
                    response_model = Response(**response_data)
                    db.session.add(response_model)
                    response_models.append(response_model)

                db.session.commit()
            except ValidationError as error:
                db.session.rollback()
                return jsonify({'errors': error.messages}), 400

        response = {
            "proposal": proposal_serializer.dump(proposal_model),
            "responses": [response_serializer.dump(response_model) for response_model in response_models]
        }

        process_proposal.delay(proposal_model.id)

        return jsonify(response), 201
    except ValidationError as e:
        db.session.rollback()
        return jsonify({'error': error.messages}), 500



# @proposal_field_bp.route('/proposal_fields', methods=["GET"])
# def get_proposal_fields():
#     serializer = ProposalFieldSchema(many=True)
#     proposal_fields = ProposalField.query.all()
#     response = serializer.dump(proposal_fields)
#     return jsonify(response), 200


# @proposal_field_bp.route('/proposal_fields/<field_name>', methods=["POST"])
# def update_proposal_field(field_name):
#     proposal_field = ProposalField.query.filter_by(name=field_name).first()
#     if not proposal_field:
#         return jsonify({'error': 'Proposal field not found'}), 404
#     proposal_field_data = request.json
#     for key, value in proposal_field_data.items():
#         setattr(proposal_field, key, value)
#     db.session.commit()
#     response = serializer.dump(proposal_field)
#     return jsonify(response), 200

# @proposal_field_bp.route('/proposal_fields/<field_name>', methods=["DELETE"])
# def delete_proposal_field(field_name):
#     proposal_field = ProposalField.query.filter_by(name=field_name).first()
#     if not proposal_field:
#         return jsonify({'error': 'Proposal field not found'}), 404
#     db.session.delete(proposal_field)
#     db.session.commit()
#     return jsonify({"message": "proposal field deleted sucessfully"}), 200

    


    
       