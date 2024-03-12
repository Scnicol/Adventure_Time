from flask import Blueprint, jsonify, session, request
from app.models import Direction, User, db
from app.forms import LoginForm
from app.forms import SignUpForm
from .auth_routes import validation_errors_to_error_messages
from flask_login import current_user, login_user, logout_user, login_required

direction_routes = Blueprint('activities', __name__)


