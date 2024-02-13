from .db import db, environment, SCHEMA, add_prefix_for_prod
from flask_login import UserMixin
from datetime import datetime

class Picture(db.Model, UserMixin):
    __tablename__ = 'pictures'

    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    adventureId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('adventures.id')), nullable=False)
    url = db.Column(db.String(300))
    isCover = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships _____________________

    adventure = db.relationship('Adventure', foreign_keys='Picture.adventureId', back_populates='pictures')

    # Methods _________________________

    def to_dict(self):
        return {
            'id': self.id,
            'adventureId': self.adventureId,
            'url': self.url,
            'isCover': self.isCover,
        }
