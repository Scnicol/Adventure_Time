from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy import CheckConstraint
from datetime import datetime

class Friend(db.Model, UserMixin):
    __tablename__ = 'friends'

    # TODO test the constraint
    __table_args__ = (
        CheckConstraint('userId1 < userId2'),
    )

    if environment == 'production':
        __table_args__ += ({'schema': SCHEMA},)

    id = db.Column(db.Integer, primary_key=True)
    userId1 = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    userId2 = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    status = db.Column(db.Enum("request_userId1","request_userId2","friend"), nullable=False)


    # Relationships _____________________

    user1 = db.relationship('User', foreign_keys='Friend.userId1', back_populates='friends1')
    user2 = db.relationship('User', foreign_keys='Friend.userId2', back_populates='friends2')

    # Methods _________________________

    def to_dict(self):
        return {
            'id': self.id,
            'status': self.status,
            'uid1': self.userId1,
            'uid2': self.userId2,
        }
