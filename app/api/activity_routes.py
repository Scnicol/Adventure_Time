from flask import Blueprint, jsonify, session, request
from app.models import User, db, Adventure, Activity
from app.forms.activity_form import ActivityForm
from datetime import datetime
from sqlalchemy import and_
from .auth_routes import validation_errors_to_error_messages
from flask_login import login_required, current_user

activity_routes = Blueprint('activities', __name__)


