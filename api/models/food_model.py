"""
Module for food item models
"""
from typing import List

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

class FoodItems():
    """
    Define food item module attributes accessed by callers
    """

    myTab = "menu"


    def add_food_item(self, item_name=None, user_id=None) -> [FoodModel]:
        """
        Add new food item to the menu
        :param item_name:
        :param user_id:
        :return:
        """
        menu_data = FoodModel(item_name, user_id)

        del menu_data.item_id

        DatabaseConnection.insert_menu_item()

        return menu_data.__dict__

    def get_menu(self)  -> [FoodModel]:
        """
        Get all menu items
        :return:
        """
        response = DatabaseConnection().get_menu_items()

        if response:
            if isinstance(response, list) and len(response) > 1:
                data = List[FoodModel] = []
                for res in response:
                    item_data = FoodModel(res['item_name'], res['user_id'])
                    item_data.item_id = res['item_id']
                    del item_data.user_id
                    data.append(item_data)
                return data
            elif isinstance(response, dict) or (isinstance(response, list) and len(response) == 1):
                if isinstance(response, list):
                    response = response[0]
                item_data1 = FoodModel(response['item_name'], response['user_id'])
                item_data1.item_status = response['item_status']
                item_data1.item_id = response['item_id']
                del item_data1.user_id
                return item_data1

        return None

    def find_item_by_name(self, item_name):
        """
        Find a specific item given it's name
        :param item_name:
        :return:
        """
        criteria = {'item_name': item_name}
        res = DataConnection().get_menu_items()
        if res and isinstance(res, dict):
            item_data = FoodModel(res['item_name'], res['user_id'])
            item_data.item_id = res["item_id"]
            return item_data
        return None
