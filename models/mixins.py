from datetime import datetime

from db.alchemy import get_db

db = get_db()

class TimeStampedModel:
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
