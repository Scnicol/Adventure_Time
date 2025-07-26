from flask import Blueprint, jsonify
from app.models import Activity, Adventure, db
from .instructionProvider import InstructionsProvider
from flask_login import login_required, current_user

activity_routes = Blueprint('activities', __name__)
provider = InstructionsProvider(Activity, 'activity', 'activities')

#GET all activities
@activity_routes.route('', methods=['GET'])
def get_all_activities():
    return provider.get_all()

#Get activity by Id
@activity_routes.route('/<int:activityId>', methods=['GET'])
def get_activity_by_id(activityId):
    return provider.get_by_id(activityId)

# New route: Get all activities created by the current user
@activity_routes.route('/user/current', methods=['GET'])
@login_required
def get_user_activities():
    user_id = current_user.get_id()
    activities = Activity.query.filter_by(creatorId=user_id).all()
    return jsonify({'activities': [activity.to_dict() for activity in activities]})

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
