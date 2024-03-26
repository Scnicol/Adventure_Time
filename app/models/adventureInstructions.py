from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class AdventureInstructions(db.Model, UserMixin):
    __instruction_column__ = 'not_set'

    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}

    adventureId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('adventures.id')), primary_key=True)
    instructionId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod(__instruction_column__)), primary_key=True)
    isUsed = db.Column(db.Boolean, default=False, nullable=False)

    # Relationships _____________________

    adventure = db.relationship('Adventures', foreign_keys='adventures.id', back_populates='activities')
    activity = db.relationship('Activities', foreign_keys=__instruction_column__, back_populates='adventures')

    # Methods _________________________

    def to_dict(self):
        return {
            'adventureId': self.adventureId,
            'isUsed': self.isUsed,
            'instructionId': self.instructionId,
        }

class AdventureActivities(AdventureInstructions):
    __tablename__ = 'adventure_activities'

    __instruction_column__ = 'activities.id'

class AdventureDirections(AdventureInstructions):
    __tablename__ = 'adventure_directions'

    __instruction_column__ = 'activities.id'
