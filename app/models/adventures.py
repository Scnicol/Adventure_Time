from .db import db, environment, SCHEMA, add_prefix_for_prod
from flask_login import UserMixin
from datetime import datetime

class Adventure(db.Model, UserMixin):
    __tablename__ = 'adventures'

    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    creatorId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(300), nullable=False)
    adventureDate = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships _____________________

    creator = db.relationship('User', foreign_keys='Adventure.creatorId', back_populates='adventures')

    pictures = db.relationship('Picture', foreign_keys='Picture.adventureId', back_populates='adventure' )

    instructionAssociations = db.relationship('AdventureInstruction', back_populates='adventure')

    # Methods _________________________

    # TODO ask chatgpt how to query a join table to improve method below
    def all_instructions(self):
        return [instructionAssociation.instruction for instructionAssociation in self.instructionAssociations]

    def to_dict(self):
        return {
            'id': self.id,
            'creatorId': self.creatorId,
            'name': self.name,
            'description': self.description,
            'createdAt': self.created_at.isoformat(),
            'updatedAt': self.updated_at.isoformat()
        }

    def to_dict_full(self):
        return {
            'id': self.id,
            'creatorId': self.creatorId,
            'name': self.name,
            'description': self.description,
            'adventureDate': self.adventureDate,
            'createdAt': self.created_at.isoformat(),
            'updatedAt': self.updated_at.isoformat(),
        }
