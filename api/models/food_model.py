"""
Module for food item models
"""

from api.models.database import DatabaseConnection
from flask_jwt_extended import jwt_required, jwt_manager, create_access_token,get_jwt_identity


class FoodModel:
    """
    Model to hold food item data
    """
    def __init__(self, item_name=None, user_id=None):
        """
        Food Item model template
        :param item_name:
        """
        self.item_id = None
        self.item_name = item_name
        self.user_id = user_id


class FoodItems:
    """
    Define food item module attributes accessed by callers
    """

    data = DatabaseConnection()

    def add_food_item(self, item_name=None, user_id=None):
        """
        Add new food item to the menu
        :param item_name:
        :param user_id:
        :return:
        """
        menu_data = FoodModel(item_name, user_id)
        self.data.insert_menu_item(item_name)

        del menu_data.item_id

        return menu_data.__dict__




