"""
Module to handle menu logic
"""
from flask import request, jsonify
from flask.views import MethodView

from api.handlers.response_errors import ResponseErrors

from api.models.food_model import FoodItems
from api.models.order_model import OrderModel
from api.utils.validation import DataValidation


class OrdersController(MethodView):
    """
    Class has special methods to handle menu logic
    """

    order_item = None
    validate = DataValidation()
    menu = FoodItems()
    orders = OrderModel()
    quantity = None

    def post(self):
        """
        Method to post an order
        :return:
         """

        post_data = request.get_json()

        key = ('order_item', 'quantity')

        if not set(key).issubset(set(post_data)):
            return ResponseErrors.missing_fields(key)

        try:
            self.order_item = post_data['order_item'].strip()
            self.quantity = post_data['quantity'].strip()

        except AttributeError:
            return ResponseErrors.invalid_data_format()
        if not self.order_item:
            return ResponseErrors.empty_data_fields()
        elif not self.DataValidation.check_item_name(self.order_item):
            return ResponseErrors.item_not_on_the_menu(self.order_item.lower())

        order = self.OrderModel.make_order(self.order_item.lower(), self.quantity)

        response_object = {
            'status': 'success',
            'message': 'Successfully posted an order',
            'data': order.__dict__
                }
        return jsonify(response_object), 201


    def get(self, order_id=None):
        """
        Method to return all existing orders
        :return:
        """

        if order_id:
            return self.get_single_order(order_id)

        current_orders = OrderModel().get_orders()

        if current_orders:
            if isinstance(current_orders, list) and len(current_orders) > 0:
                response_object = {
                    "status": "success",
                    "data": [obj.__dict__ for obj in current_orders]
                        }
                return jsonify(response_object), 200
            elif isinstance(current_orders, object):
                response_object = {
                    "status": "success",
                    "data": [current_orders.__dict__]
                        }
                return jsonify(response_object), 200
            else:
                return ResponseErrors.no_items('order')

    def get_single_order(self, order_id):
        """
        method to return a specific order
        :param order_id:
        :return:
        """
        single_order = self.orders.find_order_by_id(order_id)
        if single_order:
            response_object = {
                'status': 'success',
                'data': single_order.__dict__
            }
            return jsonify(response_object), 200
        return ResponseErrors.no_order()

    def put(self, order_id):
        """
        Method to update an order status
        :return:
        """
        post_data = request.get_json()

        key = "order_status"

        status = ['new', 'processing', 'cancelled', 'complete']

        if key not in post_data:
            return ResponseErrors.missing_fields(key)
        try:
            order_status = post_data['order_status'].strip()
        except AttributeError:
            return ResponseErrors.invalid_data_format()
        if order_status.lower() not in status:
            return ResponseErrors.order_status_not_found(order_status)
        if self.orders.find_order_by_id(order_id):
            return self.orders.update_order(order_id, order_status)
        return ResponseErrors.no_items('order')


