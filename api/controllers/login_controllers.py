"""
This module looks at the user login
"""

from flask import request, jsonify
from flask.views import MethodView
from api.utils.validation import DataValidation
from api.handlers.response_errors import ResponseErrors
from api.models.database import DatabaseConnection
from api.auth.authorise import Authenticate


class LoginControl(MethodView):
    """
    User login class with special methods to handle user login
    """
    myUser = DatabaseConnection()
    # orders = OrderModel()
    val = DataValidation()

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

        user_id = self.myUser.find_user_by_username('user_name')
        password_hash = Authenticate.hash_password(password)
        if user_id == True and password_hash == True:

            response_object = {
                'status': 'success',
                'message': 'You are logged in',
                "access_token": create_access_token(identity=user_id),
                'logged_in_as': user_id.user_type
            }
            return jsonify(response_object), 200
        else:
            response_object = {
                'status': 'fail',
                'message': 'User does not exist.'
            }
            return jsonify(response_object), 404







    # def get(self):
    #     """
    #     Method to return the order history of a user
    #     :return:
    #         """
    #
    #     order_history = self.OrderModel.order_history()
    #     if order_history:
    #         if isinstance(order_history, list):
    #             response_object = {
    #                 "status": "success",
    #                 "data": [obj.__dict__ for obj in order_history]
    #                     }
    #             return jsonify(response_object), 200
    #         elif isinstance(order_history, object):
    #
    #             response_object = {
    #                 "status": "success",
    #                 "data": [order_history.__dict__]
    #                     }
    #             return jsonify(response_object), 200
    #         else:
    #             return ResponseErrors.no_items('order')


