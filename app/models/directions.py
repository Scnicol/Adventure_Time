from .db import db, environment, SCHEMA, add_prefix_for_prod
from flask_login import UserMixin
from datetime import datetime

class Direction(db.Model, UserMixin):
    __tablename__ = 'directions'

    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    adventureId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('adventures.id')), nullable=False)
    direction = db.Column(db.String(300), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships _____________________

    adventure = db.relationship('Adventure', foreign_keys='Direction.adventureId', back_populates='directionChoices')

    # Methods _________________________

    def to_dict(self):
        return {
            'id': self.id,
            'adventureId': self.adventureId,
            'direction': self.direction,
        }
