from flask import Blueprint, make_response
from flask_wtf.csrf import generate_csrf

csrf_routes = Blueprint('csrf', __name__)

@csrf_routes.route('/csrf/restore')
def restore_csrf():
    response = make_response({'message': 'CSRF token set'})
    response.set_cookie('csrf_token', generate_csrf())
    return response
