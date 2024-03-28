from flask import Blueprint
from app.models import Direction
from .instructionProvider import InstructionsProvider
from flask_login import login_required

direction_routes = Blueprint('directions', __name__)
provider = InstructionsProvider(Direction, 'direction', 'directions')

#GET all directions
@direction_routes.route('', methods=['GET'])
def get_all_directions():
    return provider.get_all()

#Get direction by Id
@direction_routes.route('/<int:directionId>', methods=['GET'])
def get_direction_by_id(directionId):
    return provider.get_by_id(directionId)

#POST create direction
@direction_routes.route('', methods=['POST'])
@login_required
def create_direction():
    return provider.create()

#PUT Edit an direction by Id
@direction_routes.route('/<int:directionId>', methods=['PUT'])
@login_required
def update_direction_by_id(directionId):
    return provider.update_by_id(directionId)

# Delete remove an direction by directionId
@direction_routes.route('/<int:directionId>', methods=['DELETE'])
@login_required
def delete_direction(directionId):
    return provider.delete(directionId)
