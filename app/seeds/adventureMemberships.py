from app.models import db, AdventureMembership, environment, SCHEMA
from .users import *
from sqlalchemy.sql import text

def seed_adventureMemberships():
    for adventure in demo.adventures:
        for instruction in demo.instructions:
            adventure.add_instruction(instruction)

    db.session.commit()

def undo_adventureMemberships():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.{AdventureInstruction.__table_name__} RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text(f"DELETE FROM {AdventureInstruction.__table_name__}"))

    db.session.commit()
