from app.models import db, InstructionType, environment, SCHEMA
from sqlalchemy.sql import text

foodType = InstructionType(
    type = 'food'
)

activityType = InstructionType(
    type = 'activity'
)

directionsType = InstructionType(
    type = 'directions'
)

def seed_instructionTypes():
    db.session.add(foodType)
    db.session.add(activityType)
    db.session.add(directionsType)
    db.session.commit()

def undo_instructionTypes():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.instruction_types RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM instruction_types"))

    db.session.commit()
