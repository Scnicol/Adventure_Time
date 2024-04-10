from .activities import seed_activities_instructions, undo_activities_instructions
from .food import seed_food_instructions, undo_food_instructions
from .directions import seed_directions_instructions, undo_directions_instructions

def seed_instructions():
    seed_activities_instructions()
    seed_directions_instructions()
    seed_food_instructions()

def undo_instructions():
    undo_activities_instructions()
    undo_directions_instructions()
    undo_food_instructions()
