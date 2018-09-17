"""
Module to handle any logic
"""
from flask import request, jsonify
from flask.views import MethodView

from api.handlers.response_errors import ResponseErrors
from api.models.order_model import ApplicationData
from api.utils.validation import DataValidation


class OrdersController(MethodView):
    """
    Class with special methods to handle post, put and get requests
    """
    ordered_by = None
    order_items = None
    order_store = ApplicationData()
    order_status = None

    def post(self):
        """
        post method to handle post requests
        :return:
        """
        post_data = request.get_json()

        try:
            self.ordered_by = post_data["ordered_by"].strip()
            self.order_items = post_data["order_items"].strip()
        except AttributeError:
            return ResponseErrors.invalid_data_format()

        if not self.ordered_by or not self.order_items:
            return ResponseErrors.empty_data_fields()
        elif DataValidation.check_string_of_numbers(self.ordered_by) or \
                DataValidation.check_string_of_numbers(self.order_items):
            return ResponseErrors.invalid_data_format()
        current_order = self.orders.make_order(self.ordered_by, self.order_items)

        response_object = {
            'status': 'Success',
            'message': 'Your order is submitted',
            'data': current_order
        }
        return jsonify(response_object), 201


    def get(self, order_id=None):
        """
        get method to return a list of orders
        :param order_id:
        :return:
        """
        if not self.order_store.get_orders():
            return ResponseErrors.empty_data_storage()
        elif order_id:
            return self.get_order(order_id)

        response_object = {
            'status': 'success',
            'data': self.order_store.get_orders()
        }
        return jsonify(response_object), 200

    def get_order(self, order_id):
        """
        method to return a single order
        :param order_id:
        :return:
        """
        for order in self.order_store.get_orders():
            if order['order_id'] == order_id:
                response_object = {
                    'status': 'success',
                    'message': 'Order exists',
                    'data': order
                }
                return jsonify(response_object), 200

        return ResponseErrors.order_absent()