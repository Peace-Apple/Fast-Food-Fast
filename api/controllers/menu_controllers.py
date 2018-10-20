"""
Module to handle menu logic
"""
from flasgger import swag_from
from flask import request, jsonify
from flask.views import MethodView
from api.handlers.response_errors import ResponseErrors
from api.models.food_model import FoodItems
from api.utils.validation import DataValidation
from api.auth.authorise import Authenticate
from api.models.database import DatabaseConnection
from flask_jwt_extended import jwt_required, get_jwt_identity


class MenusController(MethodView):
    """
    Class has special methods to handle menu logic
    """
    item_name = None
    val = DataValidation()
    food = FoodItems()
    auth = Authenticate()
    data = DatabaseConnection()

    @jwt_required
    @swag_from('../docs/add_menu_item.yml')
    def post(self):
        """
        Method to post a menu item
        :return:
        """

        user = get_jwt_identity()
        user_type = user[4]
        user_id = user[0]

        if user_type == "TRUE" and user_id:

            post_data = request.get_json()

            key = "item_name"
            if key not in post_data:
                return ResponseErrors.missing_fields(key)
            try:
                self.item_name = post_data['item_name'].strip()
            except AttributeError:
                return ResponseErrors.invalid_data_format()

            if not self.item_name:
                return ResponseErrors.empty_data_fields()
            elif not self.val.validate_name(self.item_name):
                return ResponseErrors.invalid_name()
            elif self.val.check_item_name(self.item_name):
                return ResponseErrors.item_already_exists()

            food_data = self.food.add_food_item(self.item_name, str(user_id))

            response_object = {
                'status': '200',
                'message': 'Successfully added a new food item to the menu',
                'data': food_data
                }
            return jsonify(response_object), 200
        return ResponseErrors.denied_permission()

    @jwt_required
    @swag_from('../docs/get_menu_item.yml')
    def get(self):
        """
        Method to return existing menu items
        :return:
        """
        user = get_jwt_identity()
        user_type = user[4]
        user_id = user[0]

        if user_type == "FALSE" and user_id:

            menu_data = self.data.get_menu_items()

            if isinstance(menu_data, object):

                response_object = {
                    "msg": "successful",
                    "status": "200",
                    "data": menu_data
                    }
                return jsonify(response_object), 200
            else:
                return ResponseErrors.no_items('menu')
        return ResponseErrors.permission_denied()

