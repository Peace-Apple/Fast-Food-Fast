"""
Module to handle data storage
"""
import datetime

from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'app_secret'
jwt = JWTManager(app)


class ApplicationData:
    """
        A class that contains various methods that store data for the application
    """

    class OrderModel:

        def __init__(self):
            pass

        def register_user(self):
            pass


        def login_user(self):
            if not request.is_json:
                return jsonify({"msg": "Missing JSON in request"}), 400

            username = request.json.get('username', None)
            password = request.json.get('password', None)

            if not username:
                return jsonify({"msg": "Missing username parameter"}), 400
            if not password:
                return jsonify({"msg": "Missing password parameter"}), 400

            if username != 'test' or password != 'test':
                return jsonify({"msg": "Bad username or password"}), 401

            access_token = create_access_token(identity = username)
            return jsonify(access_token = access_token), 200


        def make_order(self):
            pass

        def get_history(self):
            pass

        def get_orders(self):
            pass

        def get_single_order(self):
            pass

        def update_order_status(self):
            pass

        def get_menu(self):
            pass

        def add_meal(self):
            pass









