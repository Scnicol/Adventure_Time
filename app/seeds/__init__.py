from flask.cli import AppGroup
from .directions import seed_directions, undo_directions
from .adventures import seed_adventures, undo_adventures
from .friends import seed_friends, undo_friends
from .users import seed_users, undo_users
from .pictures import seed_picture, undo_picture
from .instructions import seed_instructions, undo_instructions
from .adventureInstructions import seed_adventureInstructions, undo_adventureInstructions
from .adventureMemberships import seed_adventureMemberships, undo_adventureMemberships


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
        undo()

    seed_users()
    seed_adventures()
    seed_friends()
    seed_picture()
    seed_instructions()
    seed_adventureInstructions()
    seed_adventureMemberships()
    seed_directions()

    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():

    undo_adventures()
    undo_friends()
    undo_users()
    undo_picture()
    undo_instructions()
    undo_adventureInstructions()
    undo_adventureMemberships()
    undo_directions()
    # Add other undo functions here
