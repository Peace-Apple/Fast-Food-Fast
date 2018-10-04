"""
module to handle signup
"""
import copy
from flask import request, jsonify
from flask.views import MethodView
from api.handlers.response_errors import ResponseErrors
from api.models.database import DatabaseConnection
from api.models.user_model import Users
from api.utils.validation import DataValidation
from werkzeug.security import generate_password_hash, check_password_hash

class SignupControl(MethodView):
    """
    Registering a user
    """
    myUser = Users()
    val = DataValidation()

    def post(self):

        post_data = request.get_json()

        keys = ("user_name", "email", "phone_number", "password", "user_type")
        if not set(keys).issubset(set(post_data)):
            return ResponseErrors.missing_fields(keys)
        try:
            user_name = post_data.get('user_name').strip()
            email = post_data.get('email').strip()
            phone_number = post_data.get('phone_number').strip()
            password = post_data.get('password').strip()
            user_type = post_data.get('user_type').strip()
        except AttributeError:
            return ResponseErrors.invalid_data_format()

        if not user_name or not email or not phone_number or not password or not user_type:
            return ResponseErrors.empty_data_fields()
        # elif not self.val.validate_password(password, 6):
        #     return ResponseErrors.invalid_password()
        elif not self.val.validate_email(email):
            return ResponseErrors.invalid_email()
        elif not self.val.check_if_email_exists(email):
            return ResponseErrors.email_already_exists()
        elif not self.val.validate_phone(phone_number):
            return ResponseErrors.invalid_contact()
        # elif not self.val.validate_username(user_name):
        #     return ResponseErrors.invalid_name()
        elif not self.val.check_if_user_name_exists(user_name):
            return ResponseErrors.username_already_exists()
        elif not self.val.validate_user_type(user_type):
            return ResponseErrors.invalid_user_type()

        user = self.myUser.register_user(user_name, email, phone_number,
                                         Users.hash_password(password), user_type.lower())
        user = copy.deepcopy(user)
        del user.password

        response_object = {
            'status': 'success',
            'message': 'Successfully registered',
            'data': user.__dict__
                }
        return jsonify(response_object), 201
