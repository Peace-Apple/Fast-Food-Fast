"""
Module to handle menu logic
"""
from flask import request, jsonify
from flask.views import MethodView


from api.handlers.response_errors import ResponseErrors
from api.models.food_model import FoodItems
from api.utils.validation import DataValidation


class MenusController(MethodView):
    """
    Class has special methods to handle menu logic
    """
    food_item = None
    validate = DataValidation()
    food = FoodItems()

    def post(self):
        """
        Method to post a menu item
        :return:
        """

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
        elif not self.validate.validate_name(self.food_item):
            return ResponseErrors.invalid_name()
        elif self.validate.check_item_name(self.food_item):
            return ResponseErrors.item_already_exists()

        food_data = self.food.add_food_item(self.food_item.lower())

        response_object = {
                'status': 'success',
                'message': 'Successfully Added a new food item',
                'data': food_data.__dict__
                    }
        return jsonify(response_object), 201


    def get(self):
        """
        Method to return existing menu items
        :return:
        """
        menu_data = self.food_model.get_menu_items()

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

