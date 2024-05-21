from .db import db, environment, SCHEMA, add_prefix_for_prod
from flask_login import UserMixin

class AdventureMembership(db.Model, UserMixin):
    __tablename__ = 'adventure_memberships'

    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}

    adventureId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('adventures.id')), primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), primary_key=True)
    status = db.Column(db.Enum("accepted", "pending", "declined"), nullable=False)

    # Relationships _____________________

    adventure = db.relationship('Adventure', foreign_keys='AdventureMembership.adventureId', back_populates='userMemberships')
    user = db.relationship('User', foreign_keys='AdventureMembership.userId', back_populates='adventureMemberships')

    # Methods _________________________

    def to_dict(self):
        return {
            'adventureId': self.adventureId,
            'userId': self.userId,
            'status': self.status,
        }
