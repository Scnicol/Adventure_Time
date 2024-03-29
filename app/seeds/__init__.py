from flask.cli import AppGroup

from .activities import seed_activities, undo_activities
from .adventures import seed_adventures, undo_adventures
from .directions import seed_directions, undo_directions
from .food import seed_food, undo_food
from .friends import seed_friends, undo_friends
from .users import seed_users, undo_users
from .pictures import seed_picture, undo_picture

from app.models.db import db, environment, SCHEMA

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    if environment == 'production':
        # Before seeding in production, you want to run the seed undo
        # command, which will  truncate all tables prefixed with
        # the schema name (see comment in users.py undo_users function).
        # Make sure to add all your other model's undo functions below

        undo_activities()
        undo_adventures()
        undo_directions()
        undo_food()
        undo_friends()
        undo_users()
        undo_picture()

    seed_users()
    seed_adventures()
    seed_activities()
    seed_directions()
    seed_food()
    seed_friends()
    seed_picture()

    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():

    undo_activities()
    undo_adventures()
    undo_directions()
    undo_food()
    undo_friends()
    undo_users()
    undo_picture()
    # Add other undo functions here
