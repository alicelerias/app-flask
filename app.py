from os import getenv
from flask import Flask
from flask_migrate import Migrate
from db.alchemy import configure as config_db




def init_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{getenv("DB_USER")}:{getenv("DB_PASSWORD")}@{getenv("DB_HOST")}:{getenv("DB_PORT")}/{getenv("DB_NAME")}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    config_db(app)
    Migrate(app, app.db)

    return app


def create_app():
    # from models.proposal_field import ProposalField
    # from models.proposal import Proposal
    # from models.response import Response
    from views.views import bp_hello
    from views.proposal_field import proposal_field_bp
    app = init_app()
    app.register_blueprint(bp_hello)
    app.register_blueprint(proposal_field_bp)
    return app



