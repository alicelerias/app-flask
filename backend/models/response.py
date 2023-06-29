from db.alchemy import get_db
from .mixins import TimeStampedModel

db = get_db()


class Response(TimeStampedModel, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    field_name = db.Column(
        db.String(20), db.ForeignKey("proposal_field.name"), nullable=False
    )
    value = db.Column(db.Text, nullable=True)
    proposal_id = db.Column(db.Integer, db.ForeignKey("proposal.id"), nullable=False)

    proposal_field = db.relationship("ProposalField", backref="responses")
    proposal = db.relationship("Proposal", backref="responses")

    def __repr__(self):
        return f"Response(id={self.id}, value='{self.value}')"
