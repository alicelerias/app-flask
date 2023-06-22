from flask import Blueprint, current_app, request, jsonify, make_response, session
from marshmallow import ValidationError

# from models import Client
# from serializers import ClientSchema

bp_hello = Blueprint("hello", __name__)


@bp_hello.route('/', methods=['GET'])
def hello():
    return "hello world"
    