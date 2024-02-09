from app.models import db, Friend, environment, SCHEMA
from sqlalchemy.sql import text

def seed_friends():
    friend1 = Friend(
        adventureId = 1,
        friend = 'go for a hike at closest regional park'
    )

    friend2 = Friend(
        adventureId = 1,
        friend = 'pull out the basketball and shoot some hoops'
    )

    friend3 = Friend(
        adventureId = 1,
        friend = 'find the nearest beach and jump over the waves'
    )

    friend4 = Friend(
        adventureId = 1,
        friend = 'at the next stopsign or stoplight everyone get out of the car '
    )

    friend5 = Friend(
        adventureId = 1,
        friend = 'if you pulled this choose a keyword, everyone from now on has to start their sentence with the keyword. If they dont everyone else gets a point, at the end of 10 minutes most points wins'
    )

    friend6 = Friend(
        adventureId = 1,
        friend = 'stop at nearest bakery and everyone gets a sweet'
    )

    friend7 = Friend(
        adventureId = 1,
        friend = 'find nearest tennis court and play around the world for 5 minutes'
    )

    friend8 = Friend(
        adventureId = 1,
        friend = 'stop the car and everyone gets out and finds something red, bring them back and present yours'
    )

    friend9 = Friend(
        adventureId = 1,
        friend = 'find a chocolate store, get each a chocolate'
    )

    friend10 = Friend(
        adventureId = 1,
        friend = 'find lawn ornaments and take silly picture in front of them'
    )

    friend11 = Friend(
        adventureId = 2,
        friend = 'take off the bikes or rent some and do a short bike ride'
    )

    friend12 = Friend(
        adventureId = 2,
        friend = 'find the nearest beach and jump over the waves'
    )

    friend13 = Friend(
        adventureId = 2,
        friend = 'look for a local pet shop and take a peek at the inside'
    )

    friend14 = Friend(
        adventureId = 2,
        friend = 'stop at the nearest park and hop on some swings'
    )

    friend15 = Friend(
        adventureId = 2,
        friend = 'find an arcade and play a mini game'
    )

    friend16 = Friend(
        adventureId = 2,
        friend = 'call a friend and ask them to give you an friend to do'
    )

    friend17 = Friend(
        adventureId = 2,
        friend = 'go to nearest sports store and get a ball to play with, play that sport at park'
    )

    friend18 = Friend(
        adventureId = 2,
        friend = 'find a game store and look for a game you can play in the car! play one game of it'
    )

    friend19 = Friend(
        adventureId = 2,
        friend = 'go to a clothes store and get some new hats!'
    )

    friend20 = Friend(
        adventureId = 2,
        friend = 'find nearest stream or creek and look for wildlife'
    )

    friend21 = Friend(
        adventureId = 2,
        friend = 'look for a small bakeshop to get some new exciting ingredients and make something with them when you get home!'
    )

    db.session.add(friend1)
    db.session.add(friend2)
    db.session.add(friend3)
    db.session.add(friend4)
    db.session.add(friend5)
    db.session.add(friend6)
    db.session.add(friend7)
    db.session.add(friend8)
    db.session.add(friend9)
    db.session.add(friend10)
    db.session.add(friend11)
    db.session.add(friend12)
    db.session.add(friend13)
    db.session.add(friend14)
    db.session.add(friend15)
    db.session.add(friend16)
    db.session.add(friend17)
    db.session.add(friend18)
    db.session.add(friend19)
    db.session.add(friend20)
    db.session.add(friend21)

    db.session.commit()

def undo_friends():

    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.friends RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM friends"))

    db.session.commit()
