from flask import request
from app.models import User, db
from app.forms.instruction_form import InstructionForm
from .auth_routes import validation_errors_to_error_messages
from flask_login import current_user


class InstructionsProvider():
    def __init__(self, classType, modelName, pluralModelName):
        self.classType = classType
        self.modelName = modelName
        self.pluralModelName = pluralModelName


    #Get all
    def get_all(self):
        instructions = self.classType.query.all()
        return {self.pluralModelName: [instruction.to_dict() for instruction in instructions]}

    #Get by Id
    def get_by_id(self, instructionId):
        instruction = self.classType.query.get(instructionId)

        if instruction is None:
            return {'error': f'{self.modelName} not found'}, 404

        return instruction.to_dict()

    #POST create
    def create(self):
        form = InstructionForm()
        form['csrf_token'].data = request.cookies['csrf_token']

        currentUserId = current_user.get_id()
        user = User.query.get(currentUserId)

        if user is None:
            return {'error': 'User not found'}, 404

        if form.validate_on_submit() is False:
            return {'errors': validation_errors_to_error_messages(form.errors)}, 401

        newInstruction = self.classType.fromInstructions(
            instructions = form.data['instructions'],
            adventureId = form.data['adventureId'],
            creatorId = currentUserId
        )

        db.session.add(newInstruction)
        db.session.commit()
        return newInstruction.to_dict()


    #PUT Edit an activity by Id
    def update_by_id(self, instructionId):
        form = InstructionForm()
        form['csrf_token'].data = request.cookies['csrf_token']

        currentUserId = int(current_user.get_id())
        instruction = self.classType.query.get(instructionId)

        if instruction is None:
            return {'error': f'{self.modelName} could not be found'}, 404

        if instruction.creatorId != currentUserId:
            return {'error': 'User is not authorized'}, 401

        if form.validate_on_submit() is False:
            return {'errors': validation_errors_to_error_messages(form.errors)}, 401

        instruction.updateInstructions(form.data['instructions'])

        db.session.commit()

        return instruction.to_dict()


    # Delete remove an activity by activityId
    def delete(self, instructionId):
        instruction = self.classType.query.get(instructionId)

        if instruction is None:
            return {'error': f'{self.modelName} could not be found'}, 404

        if instruction.creatorId != current_user.id:
            return {'error': 'User is not authorized'}, 401

        db.session.delete(instruction)
        db.session.commit()
        return {'message': f'{self.modelName} successfully deleted'}
