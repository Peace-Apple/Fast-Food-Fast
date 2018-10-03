"""
This module looks at the user login
"""

from flask import request, jsonify
from flask.views import MethodView

from api.models.order_model import OrderModel
from api.models.user_model import Users
from api.utils.validation import DataValidation
from api.handlers.response_errors import  ResponseErrors
from api.models.database import DatabaseConnection
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity



class LoginControl(MethodView):
    """
    User login class with special methods to handle user login
    """
    myUser = Users()
    orders = OrderModel()
    validate = DataValidation()

    def post(self):
        # to get post data
        post_data = request.get_json()

        keys = ('user_name', 'password')
        if not set(keys).issubset(set(post_data)):
            return ResponseErrors.missing_fields(keys)

        try:
            user_name = post_data.get("user_name").strip()
            password = post_data.get("password").strip()
        except AttributeError:
            return ResponseErrors.invalid_data_format()

        if not user_name or not password:
            return ResponseErrors.empty_data_fields()

        user_id = self.myUser.find_user_by_username(user_name)
        password_hash = self.user_model.Users.generate_hash(password)
        if user_id and password_hash:

            response_object = {
                'status': 'success',
                'message': 'You have logged in',
                "access_token": create_access_token(identity=user_id),
                'logged_in_as': user.user_type
            }
            return jsonify(response_object), 200
        else:
            response_object = {
                'status': 'fail',
                'message': 'User does not exist.'
            }
            return jsonify(response_object), 404

