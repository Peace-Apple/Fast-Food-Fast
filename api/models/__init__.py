from flask import Flask
from api.models import order_model


app = Flask(__name__)

db_obj = order_model.DatabaseConnection()

