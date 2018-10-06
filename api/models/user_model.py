"""
Module for the user
"""

from api.models.database import DatabaseConnection

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


class Users:
    """
    Define user module attributes accessed by callers
    """
    _database_ = DatabaseConnection()


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
        self._database_.insert_user(user_name, email, phone_number, password, user_type)

        del user.user_id

        return user





