from .db import db, environment, SCHEMA, add_prefix_for_prod
from flask_login import UserMixin
from datetime import datetime
from .adventures_instructions import adventureActivitiesTable

class Activity(db.Model, UserMixin):
    __tablename__ = 'activities'

    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    creatorId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    activity = db.Column(db.String(300), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships _____________________

    adventures = db.relationship('Adventure', secondary=adventureActivitiesTable, back_populates='activities')

    # Methods _________________________

    @classmethod
    def fromInstructions(cls, instructions, adventureId, creatorId):
        return cls(activity=instructions, adventureId=adventureId, creatorId=creatorId)

    def updateInstructions(self, instructions):
        self.activity = instructions

    def to_dict(self):
        return {
            'id': self.id,
            'adventureId': self.adventureId,
            'activity': self.activity,
        }
