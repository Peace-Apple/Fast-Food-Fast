"""
Module to handle order logic
"""
from flask import request, jsonify
from flask.views import MethodView
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
    menu = FoodItems()
    orders = OrderModel()
    myorder = DatabaseConnection()


    def post(self):
        """
        Method to post an order
        :return:
         """

        # get auth_token
        auth_header = request.headers.get('Authorization')

        if self.validate.check_auth_header(auth_header):
            auth_token = self.validate.check_auth_header(auth_header)

            resp = self.auth.decode_auth_token(auth_token)

            if not isinstance(resp, str):
                post_data = request.get_json()

                key = ('order_item', 'quantity')

                if not set(key).issubset(set(post_data)):
                    return ResponseErrors.missing_fields(key)

                try:
                    self.order_item = post_data['order_item'].strip()
                    self.quantity = post_data['quantity'].strip()
                except AttributeError:
                    return ResponseErrors.invalid_data_format()
                if not self.quantity:
                    self.quantity = "No quauntity specified"

                if not self.order_item:
                    return ResponseErrors.empty_data_fields()
                elif not self.validate.check_item_name(self.order_item):
                    return ResponseErrors.item_not_on_the_menu(self.order_item.lower())

                order = self.orders.make_order(resp, self.order_item.lower(), self.quantity)

                response_object = {
                    'status': 'success',
                    'message': 'Successfully posted an order',
                    'data': order.__dict__
                }
                return jsonify(response_object), 201

            else:
                return ResponseErrors.invalid_user_token(resp)
        else:
            return ResponseErrors.user_bearer_token_error()

    def get(self, order_id=None):
        """
        Method to return all existing orders
        :return:
        """

        # get auth_token
        auth_header = request.headers.get('Authorization')
        if self.val.check_auth_header(auth_header):
            auth_token = self.val.check_auth_header(auth_header)

            resp = self.auth.decode_auth_token(auth_token)

            if not isinstance(resp, str):

                if self.val.check_user_type(resp):

                    if order_id:
                        return self.get_single_order(order_id)

                    current_orders = self.orders.get_orders()

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

                return ResponseErrors.denied_permission()
            else:
                return ResponseErrors.invalid_user_token(resp)
        else:
            return ResponseErrors.user_bearer_token_error()

    def get_single_order(self, order_id):
        """
        method to return a specific order
        :param order_id:
        :return:
        """
        single_order = self.myorder.find_order_by_id(order_id)
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

        # get auth_token
        auth_header = request.headers.get('Authorization')
        if self.val.check_auth_header(auth_header):
            auth_token = self.val.check_auth_header(auth_header)

            resp = self.auth.decode_auth_token(auth_token)

            if not isinstance(resp, str):
                if self.val.check_user_type(resp):
                    post_data = request.get_json()

                    key = "order_status"

                    status = ['new', 'processing', 'cancelled', 'completed']

                    if key not in post_data:
                        return ResponseErrors.missing_fields(key)
                    try:
                        order_status = post_data['order_status'].strip()
                    except AttributeError:
                        return ResponseErrors.invalid_data_format()

                    if order_status.lower() not in status:
                        return ResponseErrors.order_status_not_found(order_status)
                    if self.myorder.find_order_by_id(order_id):
                        return self.orders.update_order(order_id, order_status)
                    return ResponseErrors.no_items('order')

                return ResponseErrors.denied_permission()
            else:
                return ResponseErrors.invalid_user_token(resp)
        else:
            return ResponseErrors.user_bearer_token_error()



