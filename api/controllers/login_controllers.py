"""
This module looks at the user login
"""
import datetime
from flask import request, jsonify
from flask.views import MethodView
from api.utils.validation import DataValidation
from api.handlers.response_errors import ResponseErrors
from api.auth.authorise import Authenticate
from api.models.database import DatabaseConnection
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity


class LoginControl(MethodView):
    """
    User login class
    """
    data = DatabaseConnection()
    val = DataValidation()
    auth = Authenticate()

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

        user = self.data.find_user_by_username(user_name)

        if user and Authenticate.verify_password(password, user[5]):

            response_object = {
                'status': '200',
                'message': 'You are logged in',
                "access_token": create_access_token(identity=user, expires_delta=datetime.timedelta(minutes=3600)),
                'logged_in_as': str(user[1])
                }

            return jsonify(response_object)

        else:
            response_object = {
                'status': '404',
                'message': 'User does not exist.'
            }
            return jsonify(response_object)

    @jwt_required
    def get(self):
        """
        Method to return the order history of a user
        :return:
            """

        user = get_jwt_identity()
        user_type = user[4]
        user_id = user[0]

        if user_type == "FALSE" and user_id:

            order_history = self.data.get_order_history(user_id)
            if isinstance(order_history, object):

                response_object = {
                    "status": "200",
                    "msg": "success",
                    "data": order_history
                }
                return jsonify(response_object)
            else:
                return ResponseErrors.no_items('order')
        return ResponseErrors.denied_permission()


