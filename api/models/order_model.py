"""
Module to handle data storage
"""
import datetime

from flask import Flask, jsonify, request
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
        self.order_status = 'New'


class OrderModel:
    """
     Define order methods
     """
    data = DatabaseConnection()
    food = FoodItems()

    def make_order(self, user_id=None, item_id=None, order_item=None, quantity=None):
        """
        Make new order
        :param user_id:
        :param item_id:
        :param order_item:
        :param quantity:
        :return:
        """

        order_data = self.data.insert_order(user_id, item_id, order_item, quantity)

        return order_data

    def order_history(self, user_id):
        """
        Get order history of a user
        :return:
        """

        response = DatabaseConnection().get_order_history()

        if response:
            if isinstance(response, list) and len(response) > 1:
                data = List[OrderModel] = []
                for res in response:
                    order_data = OrderModel(res['order_id'], res['order_item'], res['quantity'])
                    order_data.item_id = res['item_id']
                    order_data.order_id = res['order_id']
                    order_data.order_date = res['order_date']
                    order_data.order_status = res['order_status']
                    del order_data.item_id
                    data.append(order_data)
                return data
            elif isinstance(response, dict) or (isinstance(response, list) and len(response) == 1):
                if isinstance(response, list):
                    response = response[0]
                order_data = OrderModel(response['order_id'], response['order_item'], response['quantity'])
                order_data.item_id = response['item_id']
                order_data.order_id = response['order_id']
                order_data.order_date = response['order_date']
                order_data.order_status = response['order_status']
                del order_data.item_id
                return order_data
        return None










