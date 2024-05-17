from app.models import db, AdventureMembership, User, environment, SCHEMA
from .users import *
from sqlalchemy.sql import text

def seed_adventureMemberships():
    for adventure in demo.adventures:
        for member in users.id:
            adventure.add_member(member)

    db.session.commit()

def undo_adventureMemberships():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.{AdventureMembership.__table_name__} RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text(f"DELETE FROM {AdventureMembership.__table_name__}"))

    db.session.commit()
