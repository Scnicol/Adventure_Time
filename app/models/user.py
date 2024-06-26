from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False, unique=True)
    name = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)

    # Relationships _____________________

    adventures = db.relationship('Adventure', foreign_keys='Adventure.creatorId', back_populates='creator', cascade='all, delete-orphan')
    adventureMemberships = db.relationship('AdventureMembership', foreign_keys='AdventureMembership.userId', back_populates='user', cascade='all, delete-orphan')

    friends1 = db.relationship('Friend', foreign_keys="Friend.userId1", back_populates="user1", cascade='all, delete-orphan')
    friends2 = db.relationship('Friend', foreign_keys="Friend.userId2", back_populates="user1", cascade='all, delete-orphan')
    instructions = db.relationship('Instruction', foreign_keys='Instruction.creatorId', back_populates='creator', cascade='all, delete-orphan')

  # Methods _________________________


    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }

    def memberships(self):
        all = self.query.all()
        return [member for member in all if member.status == "accepted"]
