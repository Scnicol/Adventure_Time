from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class AdventureInstruction(db.Model, UserMixin):
    __table_name__ = 'adventure_instructions'

    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}

    adventureId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('adventures.id')), primary_key=True)
    instructionId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('instructions.id')), primary_key=True)
    isUsed = db.Column(db.Boolean, default=False, nullable=False)

    # Relationships _____________________

    adventure = db.relationship('Adventure', foreign_keys='AdventureInstruction.adventureId', back_populates='instructionAssociations')
    instruction = db.relationship('Instruction', foreign_keys='AdventureInstruction.instructionId', back_populates='adventures')

    # Methods _________________________

    def to_dict(self):
        return {
            'adventureId': self.adventureId,
            'isUsed': self.isUsed,
            'instructionId': self.instructionId,
        }
