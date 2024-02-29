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

#POST create activity
@activity_routes.route('', methods=['POST'])
@login_required
def create_challenge():
    form = ActivityForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    currentUserId = current_user.get_id()
    user = User.query.get(currentUserId)

    if user is None:
        return {'error': 'User not found'}, 404

    if form.validate_on_submit():

        newActivity = Activity(
            activity = form.data['activity'],
            adventureId = form.data['adventureId']
        )

        db.session.add(newActivity)
        db.session.commit()
        return newActivity.to_dict()
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401
