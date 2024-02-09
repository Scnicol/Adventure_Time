from app.models import db, Direction, environment, SCHEMA
from sqlalchemy.sql import text

def seed_directions():
    direction1 = Direction(
        adventureId = 1,
        direction = 'follow a yellow car for 2 minutes'
    )

    direction2 = Direction(
        adventureId = 1,
        direction = 'follow a red car for 2 minutes'
    )

    direction3 = Direction(
        adventureId = 1,
        direction = 'follow a white car for 2 minutes'
    )

    direction4 = Direction(
        adventureId = 1,
        direction = 'call a friend and ask for directions for 2 minutes'
    )

    direction5 = Direction(
        adventureId = 1,
        direction = 'go right 5 times and then go straight'
    )

    direction6 = Direction(
        adventureId = 1,
        direction = 'go right then left then straight'
    )

    direction7 = Direction(
        adventureId = 1,
        direction = 'let the co-pilot steer the directions from their seat for 2 minutes'
    )

    direction8 = Direction(
        adventureId = 1,
        direction = 'follow the sun for 10 minutes'
    )

    direction9 = Direction(
        adventureId = 1,
        direction = 'follow the moon for 10 minutes'
    )

    direction10 = Direction(
        adventureId = 1,
        direction = 'roll down window and ask someone for random directions on the street'
    )

    direction11 = Direction(
        adventureId = 2,
        direction = 'each person in turn pick a direction at an intersection until everyone has done this once'
    )

    direction12 = Direction(
        adventureId = 2,
        direction = 'drive opposite the sun for 10 minutes'
    )

    direction13 = Direction(
        adventureId = 2,
        direction = 'drive opposite the moon for 10 minutes'
    )

    direction14 = Direction(
        adventureId = 2,
        direction = 'look for tallest building in the distance and try to get as close to it for 3 minutes'
    )

    direction15 = Direction(
        adventureId = 2,
        direction = 'follow nearest green car'
    )

    direction16 = Direction(
        adventureId = 2,
        direction = 'call a friend and ask them to give you a directions for 2 minutes'
    )

    direction17 = Direction(
        adventureId = 2,
        direction = 'make a wheel with turn left, turn right, go straight on it and spin it for each intersection for 2 minutes'
    )

    direction18 = Direction(
        adventureId = 2,
        direction = 'for 2 minutes if you are at a stop sign go straight, if you are at a light and its red turn left, if its green is turn right'
    )

    direction19 = Direction(
        adventureId = 2,
        direction = 'drive straight with music that has lyrics until they sing the name of the song'
    )

    direction20 = Direction(
        adventureId = 2,
        direction = 'follow the direction the wind is blowing for two minutes'
    )

    direction21 = Direction(
        adventureId = 2,
        direction = 'follow your nose! wherever it goes!'
    )

    db.session.add(direction1)
    db.session.add(direction2)
    db.session.add(direction3)
    db.session.add(direction4)
    db.session.add(direction5)
    db.session.add(direction6)
    db.session.add(direction7)
    db.session.add(direction8)
    db.session.add(direction9)
    db.session.add(direction10)
    db.session.add(direction11)
    db.session.add(direction12)
    db.session.add(direction13)
    db.session.add(direction14)
    db.session.add(direction15)
    db.session.add(direction16)
    db.session.add(direction17)
    db.session.add(direction18)
    db.session.add(direction19)
    db.session.add(direction20)
    db.session.add(direction21)

    db.session.commit()

def undo_directions():

    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.directions RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM directions"))

    db.session.commit()
