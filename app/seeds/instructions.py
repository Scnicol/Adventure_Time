from app.models import db, environment, SCHEMA
from sqlalchemy.sql import text
from .activities import seed_activities_instructions
from .food import seed_food_instructions
from .instructionTypes import seed_instructionTypes, undo_instructionTypes

def seed_instructions():
    seed_instructionTypes()
    seed_activities_instructions()
    seed_food_instructions()


def undo_instructions():
    undo_instructionTypes()

    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.instructions RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM instructions"))
    db.session.commit()
