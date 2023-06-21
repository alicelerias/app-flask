import enum

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Enum



db = SQLAlchemy()


def configure(app):
    db.init_app(app)
    app.db = db


class Choices(enum.Enum):
    texto = 'string'
    número = 'number'


class ProposalField(db.Model):
    id = db.Column(db.Integer)
    name = db.Column(db.String(80), primary_key=True, nullable=False)
    type = db.Column(Enum(Choices), nullable=False, default="string")
    nullable = db.Column(db.Boolean, nullable=False, default=True)
    order = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<Field %r>' % self.name
