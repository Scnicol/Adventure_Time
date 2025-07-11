from app.models import db, Activity, Instruction
from .instructionTypes import activityType
from sqlalchemy.sql import text

def makeActivity(creatorId, activity):
    return Activity(adventureId=1, activity=activity, creatorId=creatorId)

def makeActivityInstruction(creatorId, activity):
    return Instruction(creatorId=creatorId, instructionType=activityType, instructions=activity)

def seed_activities_instructions():
    activity_data = [
        (1, 'go for a hike at closest regional park'),
        (1, 'pull out the basketball and shoot some hoops'),
        (2, 'find the nearest beach and jump over the waves'),
        (2, 'at the next stopsign or stoplight everyone get out of the car '),
        (3, 'if you pulled this choose a keyword, everyone from now on has to start their sentence with the keyword. If they dont everyone else gets a point, at the end of 10 minutes most points wins'),
        (3, 'stop at nearest bakery and everyone gets a sweet'),
        (1, 'find nearest tennis court and play around the world for 5 minutes'),
        (1, 'stop the car and everyone gets out and finds something red, bring them back and present yours'),
        (1, 'find a chocolate store, get each a chocolate'),
        (1, 'find lawn ornaments and take silly picture in front of them'),
        (1, 'take off the bikes or rent some and do a short bike ride'),
        (1, 'find the nearest beach and jump over the waves'),
        (1, 'look for a local pet shop and take a peek at the inside'),
        (1, 'stop at the nearest park and hop on some swings'),
        (2, 'find an arcade and play a mini game'),
        (2, 'call a friend and ask them to give you an activity to do'),
        (2, 'go to nearest sports store and get a ball to play with, play that sport at park'),
        (2, 'find a game store and look for a game you can play in the car! play one game of it'),
        (3, 'go to a clothes store and get some new hats!'),
        (3, 'find nearest stream or creek and look for wildlife'),
        (3, 'look for a small bakeshop to get some new exciting ingredients and make something with them when you get home!'),
        (4, 'stop the car and everyone look for something close to the color of next upcoming holiday'),
        (4, 'Call a friend and ask them for a simple activity to do in the car'),
    ]

    activity_objs = []
    instruction_objs = []

    for creatorId, activity_text in activity_data:
        activity = makeActivity(creatorId, activity_text)
        activity_objs.append(activity)
        instruction = makeActivityInstruction(creatorId, activity_text)
        instruction_objs.append(instruction)

    db.session.add_all(activity_objs)
    db.session.add_all(instruction_objs)
    db.session.commit()

def undo_activities_instructions():
    from app.models.db import environment, SCHEMA
    if environment == "production":
        db.session.execute(text(f"TRUNCATE table {SCHEMA}.activities RESTART IDENTITY CASCADE;"))
        db.session.execute(text(f"TRUNCATE table {SCHEMA}.instructions RESTART IDENTITY CASCADE;"))
    else:
        db.session.execute(text("DELETE FROM activities;"))
        db.session.execute(text("DELETE FROM instructions;"))
    db.session.commit()
