from flask import Blueprint, jsonify, session, request
from app.models import User, db, Adventure, Activity
from app.forms.activity_form import ActivityForm
from .instructionProvider import InstructionsProvider
from datetime import datetime
from sqlalchemy import and_
from .auth_routes import validation_errors_to_error_messages
from flask_login import login_required, current_user

activity_routes = Blueprint('activities', __name__)
provider = InstructionsProvider(Activity, 'activity', 'activities')

#GET all activities
@activity_routes.route('', methods=['GET'])
def get_all_activities():
    return provider.get_all()

#Get activity by Id
@activity_routes.route('/<int:activityId>', methods=['GET'])
def get_activity_byId(activityId):
    return provider.get_by_id(activityId)

#POST create activity
@activity_routes.route('', methods=['POST'])
@login_required
def create_activity():
    return provider.create()

#PUT Edit an activity by Id
@activity_routes.route('/<int:activityId>', methods=['PUT'])
@login_required
def update_activity_by_id(activityId):
    return provider.update_by_id(activityId)

# Delete remove an activity by activityId
@activity_routes.route('/<int:activityId>', methods=['DELETE'])
@login_required
def delete_activity(activityId):
    return provider.delete(activityId)
