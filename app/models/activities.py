from .db import db, environment, SCHEMA, add_prefix_for_prod
from flask_login import UserMixin
from datetime import datetime

class Activity(db.Model, UserMixin):
    __tablename__ = 'activities'

    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    adventureId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    activity = db.Column(db.String(300), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships _____________________

    activities = db.relationship('Adventure', foreign_keys='Adventure.creatorId', back_populates='activityChoices')

    # Methods _________________________

    def to_dict(self):
        return {
            'id': self.id,
            'adventureId': self.adventureId,
            'activity': self.activity,
        }
