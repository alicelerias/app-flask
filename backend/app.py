from os import getenv
from flask import Flask
from flask_migrate import Migrate
from celery import Celery, Task
from db.alchemy import configure as config_db




def init_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{getenv("DB_USER")}:{getenv("DB_PASSWORD")}@{getenv("DB_HOST")}:{getenv("DB_PORT")}/{getenv("DB_NAME")}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config.from_mapping(
        CELERY={
            "CELERY_BROKER_URL": getenv("RABBITMQ_PORT"),
            "CELERY_RESULT_BACKEND": getenv("RABBITMQ_PORT"),
        }
    )

    config_db(app)
    Migrate(app, app.db)
    return app

def init_celery():
    class FlaskTask(Task):
        def __call__(self, *args, **kwargs) -> object:
            with app.app_context():
                return self.run(*args, **kwargs)

    app = init_app()
    celery_app = Celery(app.name, broker=getenv("RABBITMQ_PORT"), task_cls=FlaskTask)
    celery_app.config_from_object(app.config["CELERY"])
    celery_app.set_default()
    app.extensions["celery"] = celery_app
    return celery_app


def create_app():
    from views.views import bp_hello
    from views.proposal_field import proposal_field_bp
    from views.response import response_bp
    app = init_app()
    app.register_blueprint(bp_hello)
    app.register_blueprint(proposal_field_bp)
    app.register_blueprint(response_bp)
    
    return app



