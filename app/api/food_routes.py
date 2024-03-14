from flask import Blueprint
from app.models import Food
from .instructionProvider import InstructionsProvider
from flask_login import login_required

food_routes = Blueprint('food', __name__)
provider = InstructionsProvider(Food, 'food', 'food')

#GET all foods
@food_routes.route('', methods=['GET'])
def get_all_food():
    return provider.get_all()

#Get food by Id
@food_routes.route('/<int:foodId>', methods=['GET'])
def get_food_by_id(foodId):
    return provider.get_by_id(foodId)

#POST create food
@food_routes.route('', methods=['POST'])
@login_required
def create_food():
    return provider.create()

#PUT Edit an food by Id
@food_routes.route('/<int:foodId>', methods=['PUT'])
@login_required
def update_food_by_id(foodId):
    return provider.update_by_id(foodId)

# Delete remove an food by foodId
@food_routes.route('/<int:foodId>', methods=['DELETE'])
@login_required
def delete_food(foodId):
    return provider.delete(foodId)
