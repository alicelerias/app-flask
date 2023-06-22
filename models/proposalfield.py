from db.alchemy import get_db
from .mixins import TimeStampedModel


db = get_db()


class ProposalField(TimeStampedModel, db.Model):
    name = db.Column(db.String(20), primary_key=True, nullable=False)
    type = db.Column(db.String(10), nullable=False, default="string")
    nullable = db.Column(db.Boolean, nullable=False, default=True)
    order = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"field: {self.name}"
