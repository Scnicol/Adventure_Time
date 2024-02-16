from flask import Blueprint, jsonify, session, request
from app.models import Adventure, User, db
from app.forms.adventure_form import CreateAdventureForm
from datetime import datetime
from .auth_routes import validation_errors_to_error_messages
from flask_login import login_required, current_user


adventure_routes = Blueprint('adventures', __name__)

#Get all adventures
@adventure_routes.route('', methods=['GET'])
def get_all_adventures():
    adventures = Adventure.query.all()
    return {'adventures': [adventure.to_dict_full() for adventure in adventures]}

#Get all adventures made by the current user
@adventure_routes.route('/user/current', methods=['GET'])
@login_required
def get_user_adventures():
    currentUserId = current_user.get_id()
    user = User.query.get(currentUserId)

    if user is None:
        return {'error': 'User not found'}, 401

    return {'adventures': [adventure.to_dict_full() for adventure in user.adventures]}

#Get adventure by Id
@adventure_routes.route('/<int:adventureId>', methods=['GET'])
def get_adventure_by_id(adventureId):

    adventure = Adventure.query.get(adventureId)

    if adventure is None:
        return {'error': 'adventure not found'}, 404

    return adventure.to_dict_full()

#POST creat new adventure
@adventure_routes.route('', methods=['POST'])
@login_required
def create_adventure():
    form = CreateAdventureForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    currentUserId = current_user.get_id()
    user = User.query.get(currentUserId)

    if user is None:
        return {'error': 'User not found'}, 401

    if form.validate_on_submit() is False:
        return {'errors': validation_errors_to_error_messages(form.errors)}, 400

    adventureDate = form.data['adventureDate']

    if adventureDate < datetime.now().date():
        return {'errors': 'Cannot schedule an adventure in the past'}, 400

    newAdventure = Adventure(
        creatorId = currentUserId,
        name = form.data['name'],
        description = form.data['description'],
        adventureDate = form.data['adventureDate']
    )

    db.session.add(newAdventure)
    db.session.commit()
    return newAdventure.to_dict_full()
