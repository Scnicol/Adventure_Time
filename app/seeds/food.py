from app.models import db, Food, Instruction
from .instructionTypes import foodType
from sqlalchemy.sql import text

def makeFood(creatorId, food):
    return Food(adventureId=1, food=food, creatorId=creatorId)

def makeFoodInstruction(creatorId, food):
    return Instruction(creatorId=creatorId, instructionType=foodType, instructions=food)

def seed_food_instructions():
    food_data = [
        (1, 'Find nearest Mexican restaurant'),
        (1, 'Find nearest Pizza restaurant'),
        (1, 'Find nearest Hamburger restaurant'),
        (1, 'Find nearest Chinese restaurant'),
        (1, 'Find nearest Japanese restaurant'),
        (1, 'Find nearest Greek restaurant'),
        (1, 'Find nearest Italian restaurant'),
        (1, 'Find nearest Sushi restaurant'),
        (1, 'Find nearest Ethiopian restaurant'),
        (1, 'Find nearest Sandwich restaurant'),
        (2, 'Find nearest Taco restaurant'),
        (2, 'Find nearest Dumpling restaurant'),
        (2, 'Find nearest Salad restaurant'),
        (2, 'Find nearest Fish restaurant'),
        (2, 'Find nearest Michelan Star restaurant'),
        (2, 'Find nearest Kebab restaurant'),
        (2, 'Find nearest Barbeque restaurant'),
        (2, 'Find nearest Mediteranian restaurant'),
        (2, 'Find nearest Thai restaurant'),
        (2, 'Find nearest Taquerian restaurant'),
        (2, 'Find nearest Breakfast restaurant'),
        (4, 'Stop at a foodie hub and everone go bring back something around 10$ then share!'),
        (4, 'Go into store and each buy different types of food, go out and find a place to have a picnic'),
        (4, 'Stop, get out and everyone look for a place to eat, first person to find something atleast 3 people would like chooses that place to eat'),
    ]

    food_objs = []
    instruction_objs = []

    for creatorId, food_text in food_data:
        food = makeFood(creatorId, food_text)
        food_objs.append(food)
        instruction = makeFoodInstruction(creatorId, food_text)
        instruction_objs.append(instruction)

    db.session.add_all(food_objs)
    db.session.add_all(instruction_objs)
    db.session.commit()

def undo_food_instructions():
    from app.models.db import environment, SCHEMA
    if environment == "production":
        db.session.execute(text(f"TRUNCATE table {SCHEMA}.food RESTART IDENTITY CASCADE;"))
        db.session.execute(text(f"TRUNCATE table {SCHEMA}.instructions RESTART IDENTITY CASCADE;"))
    else:
        db.session.execute(text("DELETE FROM food;"))
        db.session.execute(text("DELETE FROM instructions;"))
    db.session.commit()
