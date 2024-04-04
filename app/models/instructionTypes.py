from .db import db, environment, SCHEMA, add_prefix_for_prod
from flask_login import UserMixin
from datetime import datetime

class InstructionType(db.Model, UserMixin):
    __tablename__ = 'instruction_types'

    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships _____________________

    instructions = db.relationship('Instruction', foreign_keys='Instruction.instructionTypeId', back_populates='instructionType' )

    # Methods _________________________

    def to_dict(self):
        return {
            'id': self.id,
            'adventureId': self.adventureId,
            'instructionType': self.instructionType,
            'instruction': self.instructions,
        }
