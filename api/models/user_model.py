"""
Module for the user
"""
from api.models.database import DatabaseConnection
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity


class UsersModel:
    """
    Model to hold user data
    """

    def __init__(self, user_name=None, email=None, phone_number=None, password=None, user_type=None):

        """
        User model template
        :rtype: int
        :param user_name:
        :param email:
        :param password:
        """
        self.user_name = user_name
        self.email = email
        self.password = password
        self.phone_number = phone_number
        self.user_type = user_type
        self.user_id = None


class Users():
    """
    Define user module attributes accessed by callers
    """


    def register_user(self, user_name=None, email=None, phone_number=None,
                      password=None, user_type=None):
        """
        Register new user
        :param user_name:
        :param email:
        :param phone_number:
        :param password:
        :param user_type:
        :return:
        """
        user = UsersModel(user_name, email, phone_number, password, user_type)
        DatabaseConnection.insert_user()
        return user

    def find_user_by_username(self, username):
        """
        find a specific user given a user name
        :return:
        :param username:
        :return:
        """
        pers = {'user_name': username}
        user = DatabaseConnection.get_all_users()
        if pers and isinstance(pers, dict):
            user = UsersModel(pers['user_name'], pers['email'],
                             pers['phone_number'], None, pers['user_type'])
            user.user_id = pers["user_id"]
            user.password = pers['password'].generate_password_hash()
            return user
        return None

    def find_user_by_email(self, email):
        """
        find a specific user given an email
        :param email:
        :return:
        """
        eml = {'email': email}
        res = DatabaseConnection.get_all_users()
        if res and isinstance(res, dict):
            user = UserModel(res['user_name'], res['email'],
                             res['phone_number'], None, res['user_type'])
            user.user_id = res['user_id']
            return user.email
        return None

    def find_user_by_id(self, user_id):
        """
        find a specific user given a user id
        :param user_id:
        :return:
        """
        criteria = {'user_id': user_id}
        res = DatabaseConnection().get_all_users()
        if res and isinstance(res, dict):
            user = UserModel(res['user_name'], res['email'],
                             res['contact'], None, res['user_type'])
            user.user_id = res['user_id']
            return user
        return None
