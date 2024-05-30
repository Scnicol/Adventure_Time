from app.models import db, AdventureMembership, environment, SCHEMA
from .users import *
from .adventures import *
from sqlalchemy.sql import text

def seed_adventureMemberships():
    member1 = AdventureMembership(
        adventure = adventure1, user = marnie, status = "accepted"
    )

    member2 = AdventureMembership(
        adventure = adventure1, user = bobbie, status = "declined"
    )

    member3 = AdventureMembership(
        adventure = adventure1, user = henrietta, status = "accepted"
    )

    db.session.add(member1)
    db.session.add(member2)
    db.session.add(member3)
    db.session.commit()

def undo_adventureMemberships():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.{AdventureMembership.__tablename__} RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text(f"DELETE FROM {AdventureMembership.__tablename__}"))

    db.session.commit()
