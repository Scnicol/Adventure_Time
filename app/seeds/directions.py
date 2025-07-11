from app.models import db, Direction, Instruction
from .instructionTypes import directionsType
from sqlalchemy.sql import text

def seed_directions():
    directions_data = [
        (1, 'follow a yellow car for 2 minutes'),
        (1, 'follow a red car for 2 minutes'),
        (1, 'follow a white car for 2 minutes'),
        (1, 'call a friend and ask for directions for 2 minutes'),
        (1, 'go right 5 times and then go straight'),
        (2, 'go right then left then straight'),
        (2, 'let the co-pilot steer the directions from their seat for 2 minutes'),
        (2, 'follow the sun for 10 minutes'),
        (2, 'follow the moon for 10 minutes'),
        (2, 'roll down window and ask someone for random directions on the street'),
        (2, 'each person in turn pick a directions at an intersection until everyone has done this once'),
        (3, 'drive opposite the sun for 10 minutes'),
        (3, 'drive opposite the moon for 10 minutes'),
        (3, 'look for tallest building in the distance and try to get as close to it for 3 minutes'),
        (3, 'follow nearest green car'),
        (3, 'call a friend and ask them to give you a directions for 2 minutes'),
        (1, 'make a wheel with turn left, turn right, go straight on it and spin it for each intersection for 2 minutes'),
        (1, 'for 2 minutes if you are at a stop sign go straight, if you are at a light and its red turn left, if its green is turn right'),
        (3, 'drive straight with music that has lyrics until they sing the name of the song'),
        (1, 'follow the directions the wind is blowing for two minutes'),
        (1, 'follow your nose! wherever it goes!'),
        (4, 'find the lane with the most cars and follow that lane for 3 minutes'),
    ]

    direction_objs = []
    instruction_objs = []

    for creatorId, direction_text in directions_data:
        direction = Direction(adventureId=1, direction=direction_text, creatorId=creatorId)
        direction_objs.append(direction)
        instruction = Instruction(creatorId=creatorId, instructionType=directionsType, instructions=direction_text)
        instruction_objs.append(instruction)

    db.session.add_all(direction_objs)
    db.session.add_all(instruction_objs)
    db.session.commit()

def undo_directions():
    from app.models.db import environment, SCHEMA
    if environment == "production":
        db.session.execute(text(f"TRUNCATE table {SCHEMA}.directions RESTART IDENTITY CASCADE;"))
        db.session.execute(text(f"TRUNCATE table {SCHEMA}.instructions RESTART IDENTITY CASCADE;"))
    else:
        db.session.execute(text("DELETE FROM directions;"))
        db.session.execute(text("DELETE FROM instructions;"))
    db.session.commit()
