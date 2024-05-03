from app.models import db, AdventureInstruction, environment, SCHEMA
from .users import *
from sqlalchemy.sql import text

def seed_adventureInstructions():
    for adventure in demo.adventures:
        for instruction in demo.instructions:
            adventure.add_instruction(instruction)

    db.session.commit()

def undo_adventureInstructions():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.{AdventureInstruction.__table_name__} RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text(f"DELETE FROM {AdventureInstruction.__table_name__}"))

    db.session.commit()
