from app.models import db, Picture, environment, SCHEMA
from sqlalchemy.sql import text

def seed_picture():
    picture1 = Picture(
        adventureId = 1,
        url = '',
        isCover = True
    )

    picture2 = Picture(
        adventureId = 1,
        url = '',
        isCover = False
    )

    picture3 = Picture(
        adventureId = 1,
        url = '',
        isCover = False
    )

    picture4 = Picture(
        adventureId = 1,
        url = '',
        isCover = False
    )

    picture5 = Picture(
        adventureId = 1,
        url = '',
        isCover = False
    )

    picture6 = Picture(
        adventureId = 1,
        url = '',
        isCover = False
    )

    picture7 = Picture(
        adventureId = 1,
        url = '',
        isCover = False
    )

    picture8 = Picture(
        adventureId = 1,
        url = '',
        isCover = False
    )

    picture9 = Picture(
        adventureId = 1,
        url = '',
        isCover = False
    )

    picture10 = Picture(
        adventureId = 1,
        url = '',
        isCover = False
    )

    picture11 = Picture(
        adventureId = 2,
        url = '',
        isCover = False
    )

    picture12 = Picture(
        adventureId = 2,
        url = '',
        isCover = True
    )

    picture13 = Picture(
        adventureId = 2,
        url = '',
        isCover = False
    )

    picture14 = Picture(
        adventureId = 2,
        url = '',
        isCover = False
    )

    picture15 = Picture(
        adventureId = 2,
        url = '',
        isCover = False
    )

    picture16 = Picture(
        adventureId = 2,
        url = '',
        isCover = False
    )

    picture17 = Picture(
        adventureId = 2,
        url = '',
        isCover = False
    )

    picture18 = Picture(
        adventureId = 2,
        url = '',
        isCover = False
    )

    picture19 = Picture(
        adventureId = 2,
        url = '',
        isCover = False
    )

    picture20 = Picture(
        adventureId = 2,
        url = '',
        isCover = False
    )

    picture21 = Picture(
        adventureId = 2,
        url = '',
        isCover = False
    )

    db.session.add(picture1)
    db.session.add(picture2)
    db.session.add(picture3)
    db.session.add(picture4)
    db.session.add(picture5)
    db.session.add(picture6)
    db.session.add(picture7)
    db.session.add(picture8)
    db.session.add(picture9)
    db.session.add(picture10)
    db.session.add(picture11)
    db.session.add(picture12)
    db.session.add(picture13)
    db.session.add(picture14)
    db.session.add(picture15)
    db.session.add(picture16)
    db.session.add(picture17)
    db.session.add(picture18)
    db.session.add(picture19)
    db.session.add(picture20)
    db.session.add(picture21)

    db.session.commit()

def undo_picture():

    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.pictures RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM pictures"))

    db.session.commit()
