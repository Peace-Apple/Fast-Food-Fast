"""
Module to handle validation
"""
import re #import regular expression

from api.models.food_model import FoodItems
from api.models.database import DatabaseConnection

class DataValidation:
    """
    Class has methods to handle validation of data
    """

    mydata = DatabaseConnection()


    @staticmethod
    def validate_email(email) -> bool:
        """
        Validate email address
        :param email:
        :return:
        """
        pattern = re.compile(r"^[A-Za-z0-9.+_-]+@[A-Za-z0-9._-]+\.[a-zA-Z]*$")
        if not pattern.match(email):
            return False
        return True

    def check_if_email_exists(self, email):
        """
        Check if the email already exists
        :param email:
        :return:
        """
        if self.mydata.find_user_by_email(email):
            return False
        return True

    @staticmethod
    def validate_username(name):
        """
        Username validation
        :param name:
        :return:
        """
        username_regex = re.compile("^[A-Za-z\s]{4,30}$")
        if not username_regex.match(name):
            return False
        return True

    def check_if_user_name_exists(self, username):
        """
        Check if the username already exists
        :param username:
        :return:
        """
        if self.mydata.find_user_by_username(username):
            return False
        return True

    @staticmethod
    def validate_phone(phone_number) -> bool:
        """
        Validate contact number. Must be at least 10 digits
        and not more than 13
        :param phone_number:
        :return:
        """
        phone_regex = re.compile("^[0-9]{10,13}$")
        if phone_regex.match(phone_number):
            return True
        return False

    @staticmethod
    def validate_user_type(user_type: str):
        if user_type.lower() == "admin" or user_type.lower() == "client":
            return True
        return False

    def check_user_type(self, user_id: int):
        """
        Check whether user is admin or not
        :param user_id:
        :return:
        """
        user_data = self.mydata.find_user_by_id(user_id)

        if user_data.user_type == "admin":
            return user_data
        return False

    @staticmethod
    def check_string_of_numbers(test_data):
        try:
            int(test_data)
            return True
        except ValueError:
            return False
    def check_item_name(self, item_name: str):
        """
        Check if item exists already
        :param item_name:
        :return:
        """
        if self.mydata.find_item_by_name(item_name):
            return True
        return False

    @staticmethod
    def validate_name(name):
        """
        Username validator
        :param name:
        :return:
        """
        username_regex = re.compile("^[A-Za-z\s]{4,30}$")
        if not username_regex.match(name):
            return False
        return True

    @staticmethod
    def check_auth_header(auth_header):
        if auth_header:
            try:
                auth_token = auth_header.split(' ')[1]
                return auth_token
            except IndexError:
                return None

