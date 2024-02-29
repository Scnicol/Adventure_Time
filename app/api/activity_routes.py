from flask import Blueprint, jsonify, session, request
from app.models import User, db, Adventure, Activity
from app.forms.activity_form import ActivityForm
from datetime import datetime
from sqlalchemy import and_
from .auth_routes import validation_errors_to_error_messages
from flask_login import login_required, current_user

activity_routes = Blueprint('activities', __name__)

#GET all activities
@activity_routes.route('', methods=['GET'])
def get_all_activities():
    activities = Activity.query.all()
    return {'activities': [activity.to_dict() for activity in activities]}

#Get activity by Id
@activity_routes.route('/<int:activityId>', methods=['GET'])
def get_activity_byId(activityId):
    activity = Activity.query.get(activityId)

    if activity is None:
        return {'error': 'activity not found'}, 404

    return activity.to_dict()
