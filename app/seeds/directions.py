from app.models import db, Direction
from sqlalchemy.sql import text

def seed_directions():
    d1 = Direction(adventureId=1, direction='follow a yellow car for 2 minutes', creatorId=1)
    d2 = Direction(adventureId=1, direction='follow a red car for 2 minutes', creatorId=1)
    d3 = Direction(adventureId=1, direction='follow a white car for 2 minutes', creatorId=1)
    d4 = Direction(adventureId=1, direction='call a friend and ask for directions for 2 minutes', creatorId=1)
    d5 = Direction(adventureId=1, direction='go right 5 times and then go straight', creatorId=1)
    d6 = Direction(adventureId=1, direction='go right then left then straight', creatorId=2)
    d7 = Direction(adventureId=1, direction='let the co-pilot steer the directions from their seat for 2 minutes', creatorId=2)
    d8 = Direction(adventureId=1, direction='follow the sun for 10 minutes', creatorId=2)
    d9 = Direction(adventureId=1, direction='follow the moon for 10 minutes', creatorId=2)
    d10 = Direction(adventureId=1, direction='roll down window and ask someone for random directions on the street', creatorId=2)
    d11 = Direction(adventureId=1, direction='each person in turn pick a directions at an intersection until everyone has done this once', creatorId=2)
    d12 = Direction(adventureId=1, direction='drive opposite the sun for 10 minutes', creatorId=3)
    d13 = Direction(adventureId=1, direction='drive opposite the moon for 10 minutes', creatorId=3)
    d14 = Direction(adventureId=1, direction='look for tallest building in the distance and try to get as close to it for 3 minutes', creatorId=3)
    d15 = Direction(adventureId=1, direction='follow nearest green car', creatorId=3)
    d16 = Direction(adventureId=1, direction='call a friend and ask them to give you a directions for 2 minutes', creatorId=3)
    d17 = Direction(adventureId=1, direction='make a wheel with turn left, turn right, go straight on it and spin it for each intersection for 2 minutes', creatorId=1)
    d18 = Direction(adventureId=1, direction='for 2 minutes if you are at a stop sign go straight, if you are at a light and its red turn left, if its green is turn right', creatorId=1)
    d19 = Direction(adventureId=1, direction='drive straight with music that has lyrics until they sing the name of the song', creatorId=3)
    d20 = Direction(adventureId=1, direction='follow the directions the wind is blowing for two minutes', creatorId=1)
    d21 = Direction(adventureId=1, direction='follow your nose! wherever it goes!', creatorId=1)
    d22 = Direction(adventureId=1, direction='find the lane with the most cars and follow that lane for 3 minutes', creatorId=4)

    db.session.add_all([
        d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15, d16, d17, d18, d19, d20, d21, d22
    ])
    db.session.commit()

def undo_directions():
    from app.models.db import environment, SCHEMA
    if environment == "production":
        db.session.execute(text(f"TRUNCATE table {SCHEMA}.directions RESTART IDENTITY CASCADE;"))
    else:
        db.session.execute(text("DELETE FROM directions;"))
    db.session.commit()
