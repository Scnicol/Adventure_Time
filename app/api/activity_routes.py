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


