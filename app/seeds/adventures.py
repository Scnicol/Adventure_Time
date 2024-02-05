from app.models import db, Adventure, environment, SCHEMA
from sqlalchemy.sql import text

def seed_adventures():
    adventure1 = Adventure(
        creatorId = 1,
        name = 'Rainy Day',
        description = 'Set out on a rainy day! Have fun!',
    )

    adventure2 = Adventure(
        creatorId = 2,
        name = 'Trial and Error',
        description = 'Out to have fun and do random things!'
    )

    db.session.add(adventure1)
    db.session.add(adventure2)
    db.session.commit()

def undo_adventures():

    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.adventures RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM adventures"))

    db.session.commit()
