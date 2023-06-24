import random

from celery import shared_task

from app import init_celery
from models.proposal import Proposal
from db.alchemy import get_db

db = get_db()
celery = init_celery()
log = celery.log


@shared_task()
def process_proposal(id):
    print("message received")
    try:
        proposal = Proposal.query.get(id)
        approved = bool(random.randint(0, 1))
        proposal.status = "approved" if approved else "denied"
        db.session.commit()
        print(f"Proposal {proposal.status}")
    except Proposal.DoesNotExist:
        print("Proposal not found")
    

