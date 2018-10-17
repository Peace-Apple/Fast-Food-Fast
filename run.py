"""
app root of the api endpoints. this module runs the application
"""

from flask import Flask
from api.views.routes import Urls
from api.models.database import DatabaseConnection
from flask_jwt_extended import JWTManager
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)
app.env = 'development'
Urls.generate(app)
app.config['JWT_SECRET_KEY'] = 'pass123'
jwt = JWTManager(app)


@app.before_first_request
def admin():
    my_data = DatabaseConnection()
    my_data.check_admin()


if __name__ == '__main__':
    app.run(debug=True)





