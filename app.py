from flask import Flask
from flask_migrate import Migrate
from db.alchemy import configure as config_db




def init_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/credor_flask'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    config_db(app)
    Migrate(app, app.db)

    return app


def create_app():
    from models.proposalfield import ProposalField
    from models.proposal import Proposal
    from models.response import Response
    from views import bp_hello
    app = init_app()
    app.register_blueprint(bp_hello)
    return app



