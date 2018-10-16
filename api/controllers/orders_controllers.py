"""
Module to handle order logic
"""
from flask import request, jsonify
from flask.views import MethodView
from flask_jwt_extended import jwt_required, get_jwt_identity

from api.handlers.response_errors import ResponseErrors
from api.models.food_model import FoodItems
from api.models.order_model import OrderModel
from api.utils.validation import DataValidation
from api.models.database import DatabaseConnection


class OrdersController(MethodView):
    """
    Class to handle order logic
    """

    order_item = None
    quantity = None
    val = DataValidation()
    food = FoodItems()
    orders = OrderModel()
    data = DatabaseConnection()

    @jwt_required
    def post(self):
        """
        Method to post an order
        :return:
         """
        user = get_jwt_identity()
        user_type = user[4]
        user_id = user[0]

        if user_type != "TRUE" and user_id:

            post_data = request.get_json()

            key = ('order_item', 'quantity')

            if not set(key).issubset(set(post_data)):
                return ResponseErrors.missing_fields(key)

            try:
                self.order_item = post_data['order_item'].strip()
                self.quantity = post_data['quantity'].strip()
            except AttributeError:
                return ResponseErrors.invalid_data_format()
            if not self.order_item or not self.quantity:
                return ResponseErrors.empty_data_fields()
            elif not self.val.check_item_name(self.order_item):
                return ResponseErrors.item_not_on_the_menu(self.order_item)

            item = self.data.find_item_by_name(self.order_item)

            order = self.orders.make_order(self.order_item, self.quantity, str(user_id), str(item[0]))

            if item and order:
                response_object = {
                    'status': '201',
                    'message': 'Successfully posted an order',
                    'data': order
                    }
                return jsonify(response_object)
        return ResponseErrors.denied_permission()

    @jwt_required
    def get(self, order_id=None):
        """
        Method to return all existing orders
        :param order_id:
        :return:
        """
        user = get_jwt_identity()
        user_type = user[4]
        user_id = user[0]

        if user_type == "TRUE" and user_id:
            if order_id:
                return self.data.get_a_specific_order(order_id)

            current_orders = self.data.get_all_orders()

            if isinstance(current_orders, object):

                response_object = {
                    "status": "200",
                    "msg": "success",
                    "data": current_orders
                    }
                return jsonify(response_object)
            else:
                return ResponseErrors.no_items('order')

        return ResponseErrors.denied_permission()

    @jwt_required
    def get(self, order_id):
        """
        method to return a specific order
        :param order_id:
        :return:
        """
        user = get_jwt_identity()
        user_type = user[4]
        user_id = user[0]

        if user_type == "TRUE" and user_id:

            single_order = self.data.get_a_specific_order(order_id)

            if isinstance(single_order, object):
                response_object = {
                    'status': '200',
                    'msg': 'success',
                    'data': single_order
                }
                return jsonify(response_object)

            else:
                return ResponseErrors.no_order()

        return ResponseErrors.denied_permission()

    @jwt_required
    def put(self, order_id):
        """
        Method to update an order status
        :return:
        """
        user = get_jwt_identity()
        user_type = user[4]
        user_id = user[0]

        if user_type == "TRUE" and user_id:

            post_data = request.get_json()

            key = "order_status"

            status = ['new', 'processing', 'cancelled', 'completed']

            if key not in post_data:
                return ResponseErrors.missing_fields(key)
            try:
                order_status = post_data['order_status'].strip()
            except AttributeError:
                return ResponseErrors.invalid_data_format()

            if order_status not in status:
                return ResponseErrors.order_status_not_found(order_status)
            if self.data.get_a_specific_order(order_id):

                updated_order = self.data.update_order(order_status, order_id)
                if isinstance(updated_order, object):
                    response_object = {
                        'status': '202',
                        'message': 'Status has been updated successfully'
                    }
                    return jsonify(response_object)

            return ResponseErrors.no_items('order')

        return ResponseErrors.denied_permission()




