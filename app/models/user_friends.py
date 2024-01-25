from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

class Friend(db.Model, UserMixin):
    __tablename__ = 'friends'

    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    uid1 = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    uid2 = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    status = db.Column(db.Enum("req_uid1","req_uid2","friend"))

    # Relationships _____________________

    uidf1 = db.relationship('User', foreign_keys='Friend.uid1', back_populates='uid1')
    uidf2 = db.relationship('User', foreign_keys='Friend.uid2', back_populates='uid2')

    # Methods _________________________

    def to_dict(self):
        return {
            'id': self.id,
            'status': self.status,
            'challengerId': self.currUserId,
            'challengedId': self.friendId
        }
