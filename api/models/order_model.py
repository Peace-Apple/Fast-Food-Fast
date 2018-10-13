"""
Module to handle data storage
"""
import datetime
from api.models.database import DatabaseConnection
from api.models.food_model import FoodItems


class ApplicationData:
    """
    Model to hold order data
    """

    def __init__(self, user_id=None, item_id=None, order_item=None, quantity=None):
        self.order_id = None
        self.user_id = user_id
        self.quantity = quantity
        self.order_item = order_item
        self.order_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.item_id = item_id
        self.order_status = 'new'


class OrderModel:
    """
     Define order methods
     """
    data = DatabaseConnection()
    food = FoodItems()

    def make_order(self, order_item=None, quantity=None, user_id=None, item_id=None):
        """
        Make new order
        :param order_item:
        :param quantity:
        :param user_id:
        :param item_id:
        :return:
        """

        order_data = self.data.insert_order(order_item, quantity, user_id, item_id)

        return order_data

    # def order_history(self, user_id):
    #     """
    #     Get order history of a user
    #     :return:
    #     """
    #
    #     history = self.data.get_order_history()
    #
    #     if history:
    #         if isinstance(history, list) and len(history) > 1:
    #
    #             return history
    #     return None










