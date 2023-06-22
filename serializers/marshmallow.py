from marshmallow_sqlalchemy import Marshmallow

ma = Marshmallow()

def configure(app):
    ma.init_app(app)
