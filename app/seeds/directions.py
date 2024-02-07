from app.models import db, Direction, environment, SCHEMA
from sqlalchemy.sql import text

def seed_directions():
    direction1 = Direction(
        adventureId = 1,
        direction = 'go for a hike at closest regional park'
    )

    direction2 = Direction(
        adventureId = 1,
        direction = 'pull out the basketball and shoot some hoops'
    )

    direction3 = Direction(
        adventureId = 1,
        direction = 'find the nearest beach and jump over the waves'
    )

    direction4 = Direction(
        adventureId = 1,
        direction = 'at the next stopsign or stoplight everyone get out of the car '
    )

    direction5 = Direction(
        adventureId = 1,
        direction = 'if you pulled this choose a keyword, everyone from now on has to start their sentence with the keyword. If they dont everyone else gets a point, at the end of 10 minutes most points wins'
    )

    direction6 = Direction(
        adventureId = 1,
        direction = 'stop at nearest bakery and everyone gets a sweet'
    )

    direction7 = Direction(
        adventureId = 1,
        direction = 'find nearest tennis court and play around the world for 5 minutes'
    )

    direction8 = Direction(
        adventureId = 1,
        direction = 'stop the car and everyone gets out and finds something red, bring them back and present yours'
    )

    direction9 = Direction(
        adventureId = 1,
        direction = 'find a chocolate store, get each a chocolate'
    )

    direction10 = Direction(
        adventureId = 1,
        direction = 'find lawn ornaments and take silly picture in front of them'
    )

    direction11 = Direction(
        adventureId = 2,
        direction = 'take off the bikes or rent some and do a short bike ride'
    )

    direction12 = Direction(
        adventureId = 2,
        direction = 'find the nearest beach and jump over the waves'
    )

    direction13 = Direction(
        adventureId = 2,
        direction = 'look for a local pet shop and take a peek at the inside'
    )

    direction14 = Direction(
        adventureId = 2,
        direction = 'stop at the nearest park and hop on some swings'
    )

    direction15 = Direction(
        adventureId = 2,
        direction = 'find an arcade and play a mini game'
    )

    direction16 = Direction(
        adventureId = 2,
        direction = 'call a friend and ask them to give you an direction to do'
    )

    direction17 = Direction(
        adventureId = 2,
        direction = 'go to nearest sports store and get a ball to play with, play that sport at park'
    )

    direction18 = Direction(
        adventureId = 2,
        direction = 'find a game store and look for a game you can play in the car! play one game of it'
    )

    direction19 = Direction(
        adventureId = 2,
        direction = 'go to a clothes store and get some new hats!'
    )

    direction20 = Direction(
        adventureId = 2,
        direction = 'find nearest stream or creek and look for wildlife'
    )

    direction21 = Direction(
        adventureId = 2,
        direction = 'look for a small bakeshop to get some new exciting ingredients and make something with them when you get home!'
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
