"""
Module to handle menu logic
"""
from flask import request, jsonify
from flask.views import MethodView
from api.handlers.response_errors import ResponseErrors
from api.models.food_model import FoodItems
from api.utils.validation import DataValidation
from api.auth.authorise import Authenticate
from api.models.database import DatabaseConnection


class MenusController(MethodView):
    """
    Class has special methods to handle menu logic
    """
    food_item = None
    val = DataValidation()
    food = FoodItems()
    auth = Authenticate()

    def post(self):
        """
        Method to post a menu item
        :return:
        """
        # get auth_token
        auth_header = request.headers.get('Authorization')

        if self.val.check_auth_header(auth_header):
            auth_token = self.val.check_auth_header(auth_header)

            resp = Authenticate.decode_auth_token(auth_token)

            if not isinstance(resp, str):

                if self.val.check_user_type(resp):
                    post_data = request.get_json()

                    key = "food_item"

                    if key not in post_data:
                        return ResponseErrors.missing_fields(key)

                    try:
                        self.food_item = post_data['food_item'].strip()
                    except AttributeError:
                        return ResponseErrors.invalid_data_format()

                    if not self.food_item:
                        return ResponseErrors.empty_data_fields()
                    elif not self.val.validate_name(self.food_item):
                        return ResponseErrors.invalid_name()
                    elif self.val.check_item_name(self.food_item):
                        return ResponseErrors.item_already_exists()

                    food_data = self.food.add_food_item(self.food_item.lower(), resp)

                    response_object = {
                        'status': '201',
                        'message': 'Successfully added a new food item to the menu',
                        'data': food_data.__dict__
                    }
                    return jsonify(response_object)
                return ResponseErrors.denied_permission()
            else:
                return ResponseErrors.invalid_user_token(resp)
        else:
            return ResponseErrors.user_bearer_token_error()




    def get(self):
        """
        Method to return existing menu items
        :return:
        """
        # get auth_token
        auth_header = request.headers.get('Authorization')

        if self.val.check_auth_header(auth_header):
            auth_token = self.val.check_auth_header(auth_header)

            resp = Authenticate.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                menu_data = DatabaseConnection().get_menu_items()

                if menu_data:
                    if isinstance(menu_data, list) and len(menu_data) > 0:
                        response_object = {
                            "status": "successful",
                            "data": [obj.__dict__ for obj in menu_data]
                        }
                        return jsonify(response_object), 200
                    elif isinstance(menu_data, object):

                        response_object = {
                            "status": "successful",
                            "data": [menu_data.__dict__]
                        }
                        return jsonify(response_object), 200
                else:
                    return ResponseErrors.no_items('menu')
        else:
            return ResponseErrors.user_bearer_token_error()
