"""
Authentication module for JWT token
"""
import datetime
import jwt
from flask import current_app
from api.models.user_model import Users
from werkzeug.security import generate_password_hash, check_password_hash




class Authenticate:
    """
    Class defines method used by JWT
    """
    myUser = Users()

    @staticmethod
    def encode_auth_token(user_id):
        """
        Generate auth token
        :param user_id:
        :return:
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=3600),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            val = jwt.encode(payload, "apple", algorithm='HS256')
            print(val)
            return val
        except Exception as ex:
            return ex

    @staticmethod
    def decode_auth_token(auth_token):
        """
        Decodes the auth token
        :param auth_token:
        :return:
        """

        try:
            payload = jwt.decode(auth_token, "apple")

            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'

    @staticmethod
    def hash_password(password):
        """
        method to hash password
        :param password:
        :return:
        """
        try:
            return generate_password_hash(password, method="sha256")

        except ValueError:
            return False

    @staticmethod
    def verify_password(password_text, hashed):
        """
        verify client password with stored password
        :param password_text:
        :param hashed:
        :return:
        """

        return check_password_hash(hashed, password_text)


