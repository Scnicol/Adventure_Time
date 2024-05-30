from app.models import db, Friend, environment, SCHEMA
from sqlalchemy.sql import text

def seed_friends():
    friend1 = Friend(
        userId1 = 1,
        userId2 = 2,
        status = 'friend'
    )

    friend2 = Friend(
        userId1 = 1,
        userId2 = 3,
        status = 'request_userId2'
    )

    friend3 = Friend(
        userId1 = 2,
        userId2 = 3,
        status = 'request_userId1'
    )

    friend4 = Friend(
        userId1 = 1,
        userId2 = 4,
        status = 'Friend'
    )

    db.session.add(friend1)
    db.session.add(friend2)
    db.session.add(friend3)
    db.session.add(friend4)

    db.session.commit()

def undo_friends():

    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.friends RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM friends"))

    db.session.commit()
