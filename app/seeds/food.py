from app.models import db, Instruction, environment, SCHEMA
from .instructionTypes import foodType
from sqlalchemy.sql import text

def makeFood(creatorId, food):
    return Instruction(creatorId = creatorId, instructionType = foodType, instructions = food)

def seed_food_instructions():
    food1 = Food(
        adventureId = 1,
        food = 'Find nearest Mexican restaurant'
    )

    food2 = Food(
        adventureId = 1,
        food = 'Find nearest Pizza restaurant'
    )

    food3 = Food(
        adventureId = 1,
        food = 'Find nearest Hamburger restaurant'
    )

    food4 = Food(
        adventureId = 1,
        food = 'Find nearest Chinese restaurant'
    )

    food5 = Food(
        adventureId = 1,
        food = 'Find nearest Japanese restaurant'
    )

    food6 = Food(
        adventureId = 1,
        food = 'Find nearest Greek restaurant'
    )

    food7 = Food(
        adventureId = 1,
        food = 'Find nearest Italian restaurant'
    )

    food8 = Food(
        adventureId = 1,
        food = 'Find nearest Sushi restaurant'
    )

    food9 = Food(
        adventureId = 1,
        food = 'Find nearest Ethiopian restaurant'
    )

    food10 = Food(
        adventureId = 1,
        food = 'Find nearest Sandwich restaurant'
    )

    food11 = Food(
        adventureId = 2,
        food = 'Find nearest Taco restaurant'
    )

    food12 = Food(
        adventureId = 2,
        food = 'Find nearest Dumpling restaurant'
    )

    food13 = Food(
        adventureId = 2,
        food = 'Find nearest Salad restaurant'
    )

    food14 = Food(
        adventureId = 2,
        food = 'Find nearest Fish restaurant'
    )

    food15 = Food(
        adventureId = 2,
        food = 'Find nearest Michelan Star restaurant'
    )

    food16 = Food(
        adventureId = 2,
        food = 'Find nearest Kebab restaurant'
    )

    food17 = Food(
        adventureId = 2,
        food = 'Find nearest Barbeque restaurant'
    )

    food18 = Food(
        adventureId = 2,
        food = 'Find nearest Mediteranian restaurant'
    )

    food19 = Food(
        adventureId = 2,
        food = 'Find nearest Thai restaurant'
    )

    food20 = Food(
        adventureId = 2,
        food = 'Find nearest Taquerian restaurant'
    )

    food21 = Food(
        adventureId = 2,
        food = 'Find nearest Breakfast restaurant'
    )

    db.session.add(food1)
    db.session.add(food2)
    db.session.add(food3)
    db.session.add(food4)
    db.session.add(food5)
    db.session.add(food6)
    db.session.add(food7)
    db.session.add(food8)
    db.session.add(food9)
    db.session.add(food10)
    db.session.add(food11)
    db.session.add(food12)
    db.session.add(food13)
    db.session.add(food14)
    db.session.add(food15)
    db.session.add(food16)
    db.session.add(food17)
    db.session.add(food18)
    db.session.add(food19)
    db.session.add(food20)
    db.session.add(food21)

    db.session.commit()

def undo_food_instructions():

    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.food RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM food"))

    db.session.commit()
