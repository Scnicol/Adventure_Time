from app.models import db, Instruction, environment, SCHEMA
from .instructionTypes import activityType
from sqlalchemy.sql import text

def makeActivity(creatorId, activity):
    return Instruction(creatorId = creatorId, instructionType = activityType, instructions = activity)

def seed_activities_instructions():
    activity1 = makeActivity(
        creatorId = 1,
        activity = 'go for a hike at closest regional park'
    )

    activity2 = makeActivity(
        creatorId = 1,
        activity = 'pull out the basketball and shoot some hoops'
    )

    activity3 = makeActivity(
        creatorId = 2,
        activity = 'find the nearest beach and jump over the waves'
    )

    activity4 = makeActivity(
        creatorId = 2,
        activity = 'at the next stopsign or stoplight everyone get out of the car '
    )

    activity5 = makeActivity(
        creatorId = 3,
        activity = 'if you pulled this choose a keyword, everyone from now on has to start their sentence with the keyword. If they dont everyone else gets a point, at the end of 10 minutes most points wins'
    )

    activity6 = makeActivity(
        creatorId = 3,
        activity = 'stop at nearest bakery and everyone gets a sweet'
    )

    activity7 = makeActivity(
        creatorId = 1,
        activity = 'find nearest tennis court and play around the world for 5 minutes'
    )

    activity8 = makeActivity(
        creatorId = 1,
        activity = 'stop the car and everyone gets out and finds something red, bring them back and present yours'
    )

    activity9 = makeActivity(
        creatorId = 1,
        activity = 'find a chocolate store, get each a chocolate'
    )

    activity10 = makeActivity(
        creatorId = 1,
        activity = 'find lawn ornaments and take silly picture in front of them'
    )

    activity11 = makeActivity(
        creatorId = 1,
        activity = 'take off the bikes or rent some and do a short bike ride'
    )

    activity12 = makeActivity(
        creatorId = 1,
        activity = 'find the nearest beach and jump over the waves'
    )

    activity13 = makeActivity(
        creatorId = 1,
        activity = 'look for a local pet shop and take a peek at the inside'
    )

    activity14 = makeActivity(
        creatorId = 1,
        activity = 'stop at the nearest park and hop on some swings'
    )

    activity15 = makeActivity(
        creatorId = 2,
        activity = 'find an arcade and play a mini game'
    )

    activity16 = makeActivity(
        creatorId = 2,
        activity = 'call a friend and ask them to give you an activity to do'
    )

    activity17 = makeActivity(
        creatorId = 2,
        activity = 'go to nearest sports store and get a ball to play with, play that sport at park'
    )

    activity18 = makeActivity(
        creatorId = 2,
        activity = 'find a game store and look for a game you can play in the car! play one game of it'
    )

    activity19 = makeActivity(
        creatorId = 3,
        activity = 'go to a clothes store and get some new hats!'
    )

    activity20 = makeActivity(
        creatorId = 3,
        activity = 'find nearest stream or creek and look for wildlife'
    )

    activity21 = makeActivity(
        creatorId = 3,
        activity = 'look for a small bakeshop to get some new exciting ingredients and make something with them when you get home!'
    )

    activity22 = makeActivity(
        creatorId = 4,
        activity = 'stop the car and everyone look for something close to the color of next upcoming holiday'
    )

    activity23 = makeActivity(
        creatorId = 4,
        activity = 'Call a friend and ask them for a simple activity to do in the car'
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
    db.session.add(activity22)
    db.sessions.add(activity23)

    db.session.commit()
