from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Friend(db.Model, UserMixin):
    __tablename__ = 'adventure_activities'

    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    adventureId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('adventures.id')), nullable=False)
    activityId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('activities.id')), nullable=False)
    status = db.Column(db.Enum("unused","used"), nullable=False)


    # Relationships _____________________

    user1 = db.relationship('User', foreign_keys='Friend.userId1', back_populates='userId1')
    user2 = db.relationship('User', foreign_keys='Friend.userId2', back_populates='userId2')

    # Methods _________________________

    def to_dict(self):
        return {
            'id': self.id,
            'status': self.status,
            'uid1': self.userId1,
            'uid2': self.userId2,
        }
