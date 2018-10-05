"""
Module for food item models
"""

from api.models.database import DatabaseConnection


class FoodModel:
    """
    Model to hold food item data
    """
    def __init__(self, food_item=None, user_id=None):
        """
        Food Item model template
        :param food_item:
        """
        self.item_id = None
        self.item_name = food_item
        self.user_id = user_id


class FoodItems:
    """
    Define food item module attributes accessed by callers
    """

    myTab = "menu"
    food = DatabaseConnection()

    def add_food_item(self, item_id=None, item_name=None, user_id=None):
        """
        Add new food item to the menu
        :param item_id:
        :param item_name:
        :param user_id:
        :return:
        """
        menu_data = self.food.insert_menu_item(item_id, item_name, user_id)

        del menu_data.item_id

        return menu_data.__dict__




