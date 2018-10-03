"""
Module for the user
"""

from api.models.database import DatabaseConnection


class UsersModel:
    """
    Model to hold user data
    """

    def __init__(self, user_name=None, email=None,
                 contact=None, password=None, user_type=None):

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
        self.contact = contact
        self.user_type = user_type
        self.user_id = None


class Users():
    """
    Define user module attributes accessed by callers
    """

    _table_ = "user"
    _database_ = DatabaseConnection()

    def register_user(self, user_name=None, email=None, contact=None,
                      password=None, user_type=None) -> UsersModel or None:
        """
        Register new user
        :param user_name:
        :param email:
        :param contact:
        :param password:
        :param user_type:
        :return:
        """
        user = UserModel(user_name, email, contact, password, user_type)
        user.password = user.password.decode('utf8')
        del user.user_id
        self._database_.insert(self._table_, user.__dict__)

        return user

    def find_user_by_username(self, username) -> UsersModel or None:
        """
        find a specific user given a user name
        :return:
        :param username:
        :return:
        """
        criteria = {'user_name': username}
        res = self._database_.find(self._table_, criteria=criteria)
        if res and isinstance(res, dict):
            user = UserModel(res['user_name'], res['email'],
                             res['contact'], None, res['user_type'])
            user.user_id = res["user_id"]
            user.password = res['password'].encode('utf8')
            return user
        return None

    def find_user_by_email(self, email) -> UsersModel or None:
        """
        find a specific user given an email
        :param email:
        :return:
        """
        criteria = {'email': email}
        res = self._database_.find(self._table_, criteria=criteria)
        if res and isinstance(res, dict):
            user = UserModel(res['user_name'], res['email'],
                             res['contact'], None, res['user_type'])
            user.user_id = res['user_id']
            return user.email
        return None

    def find_user_by_id(self, user_id) -> UsersModel or None:
        """
        find a specific user given a user id
        :param user_id:
        :return:
        """
        criteria = {'user_id': user_id}
        res = self._database_.find(self._table_, criteria=criteria)
        if res and isinstance(res, dict):
            user = UserModel(res['user_name'], res['email'],
                             res['contact'], None, res['user_type'])
            user.user_id = res['user_id']
            return user
        return None
