from app.models import db, Instruction, environment, SCHEMA
from .instructionTypes import directionsType
from sqlalchemy.sql import text

def makeDirections(creatorId, directions):
    return Instruction(creatorId = creatorId, instructionType = directionsType, instructions = directions)

def seed_directions_instructions():
    direction1 = makeDirections(
        directions = 'follow a yellow car for 2 minutes',
        creatorId = 1
    )

    direction2 = makeDirections(
        directions = 'follow a red car for 2 minutes',
        creatorId = 1
    )

    direction3 = makeDirections(
        directions = 'follow a white car for 2 minutes',
        creatorId = 1
    )

    direction4 = makeDirections(
        directions = 'call a friend and ask for directions for 2 minutes',
        creatorId = 1
    )

    direction5 = makeDirections(
        directions = 'go right 5 times and then go straight',
        creatorId = 1
    )

    direction6 = makeDirections(
        directions = 'go right then left then straight',
        creatorId = 2
    )

    direction7 = makeDirections(
        directions = 'let the co-pilot steer the directions from their seat for 2 minutes',
        creatorId = 2
    )

    direction8 = makeDirections(
        directions = 'follow the sun for 10 minutes',
        creatorId = 2
    )

    direction9 = makeDirections(
        directions = 'follow the moon for 10 minutes',
        creatorId = 2
    )

    direction10 = makeDirections(
        directions = 'roll down window and ask someone for random directions on the street',
        creatorId = 2
    )

    direction11 = makeDirections(
        directions = 'each person in turn pick a directions at an intersection until everyone has done this once',
        creatorId = 2
    )

    direction12 = makeDirections(
        directions = 'drive opposite the sun for 10 minutes',
        creatorId = 3
    )

    direction13 = makeDirections(
        directions = 'drive opposite the moon for 10 minutes',
        creatorId = 3
    )

    direction14 = makeDirections(
        directions = 'look for tallest building in the distance and try to get as close to it for 3 minutes',
        creatorId = 3
    )

    direction15 = makeDirections(
        directions = 'follow nearest green car',
        creatorId = 3
    )

    direction16 = makeDirections(
        directions = 'call a friend and ask them to give you a directions for 2 minutes',
        creatorId = 3
    )

    direction17 = makeDirections(
        directions = 'make a wheel with turn left, turn right, go straight on it and spin it for each intersection for 2 minutes',
        creatorId = 1
    )

    direction18 = makeDirections(
        directions = 'for 2 minutes if you are at a stop sign go straight, if you are at a light and its red turn left, if its green is turn right',
        creatorId = 1
    )

    direction19 = makeDirections(
        directions = 'drive straight with music that has lyrics until they sing the name of the song',
        creatorId = 3
    )

    direction20 = makeDirections(
        directions = 'follow the directions the wind is blowing for two minutes',
        creatorId = 1
    )

    direction21 = makeDirections(
        directions = 'follow your nose! wherever it goes!',
        creatorId = 1
    )

    direction22 = makeDirections(
        directions = "find the lane with the most cars and follow that lane for 3 minutes",
        creatorId = 4
    )

    db.session.add(direction1)
    db.session.add(direction2)
    db.session.add(direction3)
    db.session.add(direction4)
    db.session.add(direction5)
    db.session.add(direction6)
    db.session.add(direction7)
    db.session.add(direction8)
    db.session.add(direction9)
    db.session.add(direction10)
    db.session.add(direction11)
    db.session.add(direction12)
    db.session.add(direction13)
    db.session.add(direction14)
    db.session.add(direction15)
    db.session.add(direction16)
    db.session.add(direction17)
    db.session.add(direction18)
    db.session.add(direction19)
    db.session.add(direction20)
    db.session.add(direction21)
    db.session.add(direction22)

    db.session.commit()
