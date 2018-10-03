"""
This module looks at the user login
"""

from flask import request, jsonify
from flask.views import MethodView

from api.models.order_model import OrderModel
from api.models.user_model import Users
from api.utils.validation import DataValidation
from api.handlers.response_errors import  ResponseErrors



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

        user = self.user.find_user_by_username(user_name)

        if user and self.auth.verify_password(password, user.password):
            auth_token = self.auth.encode_auth_token(user.user_id)
            response_object = {
                'status': 'success',
                'message': 'You have logged in',
                'auth_token': auth_token.decode(),
                'logged_in_as': user.user_type
            }
            return jsonify(response_object), 200
        else:
            response_object = {
                'status': 'fail',
                'message': 'User does not exist.'
            }
            return jsonify(response_object), 404

    def get(self):
        """
        Method to return the order history of a user
        :return:
        """

        # get auth_token
        auth_header = request.headers.get('Authorization')
        if self.validate.check_auth_header(auth_header):
            auth_token = self.validate.check_auth_header(auth_header)

            resp = self.auth.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                order_history = self.orders.order_history(resp)
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
                    return ReturnError.no_items('order')
            else:
                return ReturnError.invalid_user_token(resp)
        else:
            return ReturnError.user_bearer_token_error()
