"""
This module looks at the user login
"""
from flask import request, jsonify
from flask.views import MethodView
from api.utils.validation import DataValidation
from api.handlers.response_errors import ResponseErrors
from api.auth.authorise import Authenticate
from api.models.order_model import OrderModel
from api.models.database import DatabaseConnection


class LoginControl(MethodView):
    """
    User login class with special methods to handle user login
    """
    my_user = DatabaseConnection()
    val = DataValidation()
    auth = Authenticate()
    orders = OrderModel()

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

        user = self.my_user.find_user_by_username(user_name)

        if user and Authenticate.verify_password(password, user[5]):

            response_object = {
                'status': '200',
                'message': 'You are logged in',
                "access_token": str(Authenticate.encode_auth_token(user[0])),
                'logged_in_as': str(user[1])
                }

            return jsonify(response_object)

        else:
            response_object = {
                'status': '404',
                'message': 'User does not exist.'
            }
            return jsonify(response_object)

    def get(self):
        """
        Method to return the order history of a user
        :return:
            """

        order_history = self.orders.order_history()
        if order_history:
            if isinstance(order_history, list):
                response_object = {
                    "status": "success",
                    "data": [obj.__dict__ for obj in order_history]
                        }
                return jsonify(response_object), 200
            elif isinstance(order_history, object):

                response_object = {
                    "status": "success",
                    "data": [order_history.__dict__]
                        }
                return jsonify(response_object), 200
            else:
                return ResponseErrors.no_items('order')


