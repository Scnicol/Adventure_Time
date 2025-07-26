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
    print('DEBUG currentUserId:', currentUserId)
    user = User.query.get(currentUserId)
    print('DEBUG user:', user)
    print('DEBUG user.adventures:', user.adventures if user else None)

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

#PUT edit an adventure by Id
@adventure_routes.route('/<int:adventureId>', methods=['PUT'])
@login_required
def edit_adventure_by_id(adventureId):
    form = CreateAdventureForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    adventure = Adventure.query.get(adventureId)

    if adventure is None:
        return {'error': 'Adventure could not be found'}, 404

    if adventure.creatorId != current_user.id:
        return {'error': 'User is not authorized'}, 401

    if form.validate_on_submit() is False:
        return {'errors': validation_errors_to_error_messages(form.errors)}, 400

    adventureDate = form.data['adventureDate']
    if adventureDate < datetime.now().date():
        return {'errors': 'Cannot schedule an adventure in the past'}, 400

    adventure.name = form.data['name']
    adventure.description = form.data['description']
    adventure.adventureDate = form.data['adventureDate']

    db.session.commit()

    return adventure.to_dict_full()

#DELETE remove an adventure by adventureId
@adventure_routes.route('/<int:adventureId>', methods=['DELETE'])
@login_required
def delete_adventure(adventureId):
    adventure = Adventure.query.get(adventureId)

    if adventure is None:
        return {'error': 'Adventure could not be found'}, 404

    if adventure.creatorId != current_user.id:
        return {'error': 'User is not authorized'}, 401

    db.session.delete(adventure)
    db.session.commit()
    return {'message': 'Adventure successfully deleted'}

#Get all adventures the current user has joined (not created)
@adventure_routes.route('/user/current/joined', methods=['GET'])
@login_required
def get_user_joined_adventures():
    currentUserId = current_user.get_id()
    user = User.query.get(currentUserId)

    if user is None:
        return {'error': 'User not found'}, 401

    # Adventures where user is a member (status accepted) but not the creator
    joined_adventures = []
    for membership in user.adventureMemberships:
        if membership.status == 'accepted':
            adventure = membership.adventure
            if adventure.creatorId != int(currentUserId):
                joined_adventures.append(adventure.to_dict_full())

    return {'adventures': joined_adventures}
