from flask import Blueprint, jsonify, session, request
from app.models import Adventure, db
from app.forms import adventure_form
from flask_login import login_required, current_user


adventure_routes = Blueprint('adventures', __name__)

#Get all adventures
@adventure_routes.route('', methods=['GET'])
def get_all_adventures():
    adventures = Adventure.query.all()
    return {'adventures': [adventure.to_dict_full() for adventure in adventures]}
