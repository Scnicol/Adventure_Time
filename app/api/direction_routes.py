from flask import Blueprint, jsonify, session, request
from app.models import Direction, User, db
from .instructionProvider import InstructionsProvider
from app.forms import LoginForm
from app.forms import SignUpForm
from .auth_routes import validation_errors_to_error_messages
from flask_login import current_user, login_user, logout_user, login_required

direction_routes = Blueprint('directions', __name__)
provider = InstructionsProvider(Direction, 'direction')

#GET all directions
@direction_routes.route('', methods=['GET'])
def get_all_directions():
    return provider.get_all('directions')

#GET direction by Id
@direction_routes.route('/<int:directionId>', method=['GET'])
def get_direction_by_id(directionId):
    direction = Direction.query.get(directionId)

    if direction is None:
        return {'error', 'direction not found'}, 401

    return direction.to_dict()
