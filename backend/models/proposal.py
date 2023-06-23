
from db.alchemy import get_db
from .mixins import TimeStampedModel


db = get_db()


class Proposal(TimeStampedModel, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f"proposal: {self.id}"
