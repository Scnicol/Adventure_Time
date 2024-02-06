from app.models import db, Activity, environment, SCHEMA
from sqlalchemy.sql import text

def seed_activities():
    activity1 = Activity(
        adventureId = 1,
        activity = 'go for a hike at closest regional park'
    )

    activity2 = Activity(
        adventureId = 1,
        activity = 'pull out the basketball and shoot some hoops'
    )

    activity3 = Activity(
        adventureId = 1,
        activity = 'find the nearest beach and jump over the waves'
    )

    activity4 = Activity(
        adventureId = 1,
        activity = 'at the next stopsign or stoplight everyone get out of the car '
    )

    activity5 = Activity(
        adventureId = 1,
        activity = 'if you pulled this choose a keyword, everyone from now on has to start their sentence with the keyword. If they dont everyone else gets a point, at the end of 10 minutes most points wins'
    )

    activity6 = Activity(
        adventureId = 1,
        activity = 'stop at nearest bakery and everyone gets a sweet'
    )

    activity7 = Activity(
        adventureId = 1,
        activity = 'find nearest tennis court and play around the world for 5 minutes'
    )

    activity8 = Activity(
        adventureId = 1,
        activity = 'stop the car and everyone gets out and finds something red, bring them back and present yours'
    )

    activity9 = Activity(
        adventureId = 1,
        activity = 'find a chocolate store, get each a chocolate'
    )

    activity10 = Activity(
        adventureId = 1,
        activity = 'find lawn ornaments and take silly picture in front of them'
    )

    activity11 = Activity(
        adventureId = 2,
        activity = 'take off the bikes or rent some and do a short bike ride'
    )

    activity12 = Activity(
        adventureId = 2,
        activity = 'find the nearest beach and jump over the waves'
    )

    activity13 = Activity(
        adventureId = 2,
        activity = 'look for a local pet shop and take a peek at the inside'
    )

    activity14 = Activity(
        adventureId = 2,
        activity = 'stop at the nearest park and hop on some swings'
    )

    activity15 = Activity(
        adventureId = 2,
        activity = 'find the nearest beach and jump over the waves'
    )

    activity16 = Activity(
        adventureId = 2,
        activity = 'find the nearest beach and jump over the waves'
    )

    activity17 = Activity(
        adventureId = 2,
        activity = 'find the nearest beach and jump over the waves'
    )

    activity18 = Activity(
        adventureId = 2,
        activity = 'find the nearest beach and jump over the waves'
    )

    activity19 = Activity(
        adventureId = 2,
        activity = 'find the nearest beach and jump over the waves'
    )

    activity20 = Activity(
        adventureId = 2,
        activity = 'find the nearest beach and jump over the waves'
    )

    activity21 = Activity(
        adventureId = 2,
        activity = 'find the nearest beach and jump over the waves'
    )

    db.session.add(activity1)
    db.session.add(activity2)
    db.session.add(activity3)
    db.session.add(activity4)
    db.session.add(activity5)
    db.session.add(activity6)
    db.session.add(activity7)
    db.session.add(activity8)
    db.session.add(activity9)
    db.session.add(activity10)
    db.session.add(activity11)
    db.session.add(activity12)
    db.session.add(activity13)
    db.session.add(activity14)
    db.session.add(activity15)
    db.session.add(activity16)
    db.session.add(activity17)
    db.session.add(activity18)
    db.session.add(activity19)
    db.session.add(activity20)
    db.session.add(activity21)

    db.session.commit()

def undo_activies():

    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.activities RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM activities"))

    db.session.commit()
