"""
Module for the user
"""

from api.models.database import DatabaseConnection


class UsersModel:
    """
    Model to hold user data
    """

    def __init__(self, user_name=None, email=None, phone_number=None, password=None):

        """
        User model template
        :param user_name:
        :param email:
        :param phone_number:
        :param password:
        """
        self.user_name = user_name
        self.email = email
        self.password = password
        self.phone_number = phone_number
        self.user_type = None
        self.user_id = None


class Users:
    """
    Define user module attributes accessed by callers
    """
    my_data = DatabaseConnection()

    def register_user(self, user_name=None, email=None, phone_number=None, password=None):
        """
        Register new user
        :param user_name:
        :param email:
        :param phone_number:
        :param password:
        :return:
        """
        user = UsersModel(user_name, email, phone_number, password)
        self.my_data.insert_user(user_name, email, phone_number, password)

        del user.user_id

        return user




