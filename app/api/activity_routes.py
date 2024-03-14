from flask import Blueprint, jsonify, session, request
from app.models import User, db, Adventure, Activity
from app.forms.activity_form import ActivityForm
from .instruction import InstructionsProvider
from datetime import datetime
from sqlalchemy import and_
from .auth_routes import validation_errors_to_error_messages
from flask_login import login_required, current_user

activity_routes = Blueprint('activities', __name__)
provider = InstructionsProvider(Activity, 'activity')

#GET all activities
@activity_routes.route('', methods=['GET'])
def get_all_activities():
    return provider.get_all('activities')

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
def update_activity_byId(activityId):
    form = ActivityForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    currentUserId = current_user.get_id()
    activity = Activity.query.get(activityId)

    if activity is None:
        return {'error': 'Activity could not be found'}, 404

    if activity.creatorId != currentUserId:
        return {'error': 'User is not authorized'}, 401

    if form.validate_on_submit():

        activity.activity = form.data['activity']

        db.session.commit()

        return activity.to_dict()
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401

# Delete remove an activity by activityId
@activity_routes.route('/<int:activityId>', methods=['DELETE'])
@login_required
def delete_activity(activityId):
    activity = Activity.query.get(activityId)

    if activity is None:
        return {'error': 'Activity could not be found'}, 404

    if activity.creatorId != current_user.id:
        return {'error': 'User is not authorized'}, 401

    db.session.delete(activity)
    db.session.commit()
    return {'message': 'Activity successfully deleted'}
