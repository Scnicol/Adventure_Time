from flask import Blueprint, jsonify, session, request
from app.models import Adventure, User, db
from app.forms import adventure_form
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
