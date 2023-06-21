from flask import Flask
from flask_migrate import Migrate
from models import configure as config_db




def init_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/credor_flask'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    config_db(app)
    Migrate(app, app.db)

    return app


def create_app():
    app = init_app()

    from models import ProposalField
    from views import bp_hello
    app.register_blueprint(bp_hello)
    return app



