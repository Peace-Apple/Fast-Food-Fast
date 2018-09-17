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
    orders = ApplicationData()

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

