from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Adventure_activities(db.Model, UserMixin):
    __tablename__ = 'adventure_activities'

    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    adventureId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('adventures.id')), nullable=False)
    activityId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('activities.id')), nullable=False)
    status = db.Column(db.Enum("unused","used"), nullable=False)


    # Relationships _____________________

    adventures = db.relationship('User', foreign_keys='Adventure.id', back_populates='activities')
    activities = db.relationship('User', foreign_keys='Activities.id', back_populates='adventures')

    # Methods _________________________

    def to_dict(self):
        return {
            'id': self.id,
            'adventureId': self.adventureId,
            'status': self.status,
            'activityId': self.activityId,
        }
