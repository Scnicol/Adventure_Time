from .db import db, environment, SCHEMA, add_prefix_for_prod
from flask_login import UserMixin
from datetime import datetime

class Instruction(db.Model, UserMixin):
    __tablename__ = 'instructions'

    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    creatorId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    instructionTypeId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('instruction_types.id')), nullable=False)
    instructions = db.Column(db.String(300), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships _____________________

    instructionType = db.relationship('InstructionType', foreign_keys='Instruction.instructionTypeId', back_populates='instructions' )
    creator = db.relationship('Instruction', foreign_keys='Instruction.creatorId', back_populates='instructions')

    adventureAssociations = db.relationship('AdventureInstruction', foreign_keys='AdventureInstruction.instructionId', back_populates='instruction')

    # Methods _________________________

    # TODO search for ways to make this a more efficient query (where type)
    @classmethod
    def allForType(cls, type):
        all = cls.query.all()
        return [instruction for instruction in all if instruction.instructionType.name == type]

    def to_dict(self):
        return {
            'id': self.id,
            'adventureId': self.adventureId,
            'instructionType': self.instructionType.name,
            'instruction': self.instructions,
        }
