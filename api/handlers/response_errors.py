"""
Module to handle all error responses
"""
from flask import jsonify, request


class ResponseErrors:
    """
        Error handler to handle response errors.
        """

    @staticmethod
    def missing_fields(key):
        response_object = {
            "status": "fail",
            "error_message": "some fields are missing" + key
                   }
        return jsonify(response_object), 400

    @staticmethod
    def invalid_data_format():
        response_object = {
            'status': 'fail',
            'error_message': 'Please use character strings'
        }
        return jsonify(response_object), 400

    @staticmethod
    def empty_data_fields():
        response_object = {
            'status': 'fail',
            'error_message': 'Some fields have no data'
        }
        return jsonify(response_object), 400

    @staticmethod
    def empty_data_storage():
        response_object = {
            'status': 'fail',
            'message': 'No orders currently'
           }
        return jsonify(response_object), 200

    @staticmethod
    def order_absent():
        response_object = {
            'status': 'fail',
            'error_message': 'Order does not exist'
             }
        return jsonify(response_object), 400

    @staticmethod
    def missing_key(keys):
        response_object = {
            'status': 'fail',
            'error_message': 'Missing key ' + keys,
        }
        return jsonify(response_object), 400

    @staticmethod
    def invalid_password():
        response_object = {
            "status": "fail",
            "error_message": "Password is wrong. It should be at-least 6 characters"
                             " long, and alphanumeric."
        }
        return jsonify(response_object), 400

    @staticmethod
    def invalid_email():
        return jsonify({
            "status": "fail",
            "error_message": "User email {0} is wrong, It should be "
                             "in the format (xxxxx@xxxx.xxx)"

        }), 400

    @staticmethod
    def invalid_contact():
        return jsonify({"error_message": "Contact {0} is wrong. should be in"
                                         " the form, (070******) and between 10 and 13 "
                                         "digits"
                        }), 400

    @staticmethod
    def username_already_exists():
        response_object = {
            'status': 'fail',
            'error_message': 'Username already taken',


        }
        return jsonify(response_object), 409

    @staticmethod
    def email_already_exists():
        response_object = {
            'status': 'fail',
            'error_message': 'email already exists'

                }
        return jsonify(response_object), 409

    @staticmethod
    def item_already_exists():
        response_object = {
            'status': 'fail',
            'error_message': 'Item already exists'

        }
        return jsonify(response_object),400

    @staticmethod
    def item_not_on_the_menu(order_item):
        response_object = {
            'status': 'fail',
            'error_message': 'Sorry, Order item {} not on the menu'.format(order_item)
        }
        return jsonify(response_object), 400

    @staticmethod
    def invalid_name():
        return jsonify({
            "status": "fail",
            "error_message": "A name should consist of only alphabetic characters"
                   }), 400

    @staticmethod
    def invalid_user_type():
        req = request.get_json()
        return jsonify({
            "status": "fail",
            "error_message": "User type {0} does not exist ".format(req['user_type']),
            "data": req
        }),  400

    @staticmethod
    def no_items(item):
        response_object = {
            'status': 'fail',
            'message': 'No {} items currently'.format(item)
        }
        return jsonify(response_object), 200

    @staticmethod
    def user_bearer_token_error():
        response_object = {
            'status': 'fail',
            'message': 'Bearer token malformed'
        }
        return jsonify(response_object), 401

    @staticmethod
    def order_item_absent():
        response_object = {
            'status': 'fail',
            'message': 'Order item not found'
        }
        return jsonify(response_object), 404

    @staticmethod
    def no_order():
        return jsonify({
            "status": "fail",
            "message": "Order not found"
                    }), 404

    @staticmethod
    def order_status_not_found(order_status):
        return jsonify({
            "status": "fail",
            "error_message": "Order status {} not found".format(order_status),
            }), 404

    @staticmethod
    def denied_permission():
        response_object = {
            'status': 'fail',
            'message': 'Permission denied, Please Login as Admin'
        }
        return jsonify(response_object), 403

    @staticmethod
    def invalid_user_token(resp):
        response_object = {
            'status': 'fail',
            'message': resp
        }
        return jsonify(response_object), 401
