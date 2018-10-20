 """
Tests module
"""
from flask import json

from unittest import TestCase

from run import app


class TestFastFoodFast(TestCase):
    """
       Tests run for the api
       """

    def setUp(self):
        self.app = app
        self.client = self.app.test_client

    def register_user(self, user_name=None, email=None, phone_number=None, password=None):
        return self.client().post(
            '/api/v2/auth/signup/',
            data=json.dumps(dict(
                user_name=user_name,
                email=email,
                phone_number=phone_number,
                password=password,
            )),
            content_type="application/json"
        )

    def login_user(self, user_name=None, password=None):
        return self.client().post(
            '/api/v2/auth/login/',
            data=json.dumps(dict(
                user_name=user_name,
                password=password,
            )),
            content_type='application/json'
        )

    # def test_user_registration(self):
    #     """
    #     Test successful user signup
    #     :return:
    #     """
    #     register = self.register_user('Apple', 'apple@gmail.com', '0704194672', 'pesay')
    #     received_data = json.loads(register.data.decode())
    #     self.assertTrue(received_data['status'], 'success')
    #     self.assertTrue(received_data['message'], 'Your account has been created successfully')
    #     self.assertTrue(received_data['data'])
    #     self.assertTrue(register.content_type, 'application/json')
    #     self.assertEqual(register.status_code, 201)

    def test_missing_fields_during_signup(self):
        """
        Test for missing fields when registering a new user
        :return:
        """
        register = self.client().post(
            '/api/v2/auth/signup/',
            data=json.dumps(dict(
                user_name='Apple',
                email='apple@gmail.com',
                phone_number='0704194672',
            )),
            content_type="application/json"
        )
        response_data = json.loads(register.data.decode())
        self.assertTrue(response_data['status'], 'fail')
        self.assertTrue(response_data['error_message'], 'some fields are missing')
        self.assertTrue(response_data['data'])
        self.assertTrue(register.content_type, 'application/json')
        self.assertEqual(register.status_code, 400)

    def test_invalid_data_type(self):
        """
        Test user registration with invalid data-type
        :return:
        """
        register = self.register_user(10000, 'apple@gmail.com', '0704194672', 'pesay')
        received_data = json.loads(register.data.decode())
        self.assertTrue(received_data['status'], 'fail')
        self.assertTrue(received_data['error_message'], 'Please use character strings')
        self.assertFalse(received_data['data'])
        self.assertTrue(register.content_type, 'application/json')
        self.assertEqual(register.status_code, 400)

    def test_empty_fields_during_signup(self):
        """
        Test for empty fields during user registration
        :return:
        """
        register = self.register_user(' ', 'apple@gmail.com', '0704194672', 'pesay')
        response_data = json.loads(register.data.decode())
        self.assertTrue(response_data['status'], 'fail')
        self.assertTrue(response_data['error_message'], 'Some fields have no data')
        self.assertTrue(response_data['data'])
        self.assertTrue(register.content_type, 'application/json')
        self.assertEqual(register.status_code, 400)

    # def test_invalid_password(self):
    #     """
    #     Test for password less than 5 characters
    #     :return:
    #     """
    #     register = self.register_user('Apple', 'apple@gmail.com', '0704194672', 'pesay')
    #     response_data = json.loads(register.data.decode())
    #     self.assertTrue(response_data['status'], 'fail')
    #     self.assertTrue(response_data['error_message'],
    #                     'Password is wrong. It should be at-least 5 characters long, and alphanumeric.')
    #     self.assertTrue(response_data['data'])
    #     self.assertTrue(register.content_type, 'application/json')
    #     self.assertEqual(register.status_code, 400)

    def test_invalid_email_registration(self):
        """
        Test for registration with invalid email
        :return:
        """
        register = self.register_user('Apple', 'apple@gmail', '0704194672', 'pesay')
        response_data = json.loads(register.data.decode())
        self.assertTrue(response_data['status'], 'fail')
        self.assertTrue(response_data['error_message'], 'User email {0} is wrong,'
                                                        'It should be in the format (xxxxx@xxxx.xxx)')
        self.assertTrue(response_data['data'])
        self.assertTrue(register.content_type == "application/json")
        self.assertEqual(register.status_code, 400)

    # def test_invalid_phone_number(self):
    #     """
    #     testing invalid phone_number
    #     :return:
    #     """
    #     register = self.register_user('Apple', 'apple@gmail.com', '070419', 'pesay')
    #     received_data = json.loads(register.data.decode())
    #     self.assertTrue(received_data['status'], 'fail')
    #     self.assertTrue(received_data['error_message'], 'Contact {0} is wrong. should be in the form, (070*******)'
    #                                                     'and between 10 and 13 digits')
    #     self.assertTrue(received_data['data'])
    #     self.assertTrue(register.content_type, 'application/json')
    #     self.assertEqual(register.status_code, 400)

    def test_invalid_user_name(self):
        """
        testing invalid username
        :return:
        """
        register = self.register_user('Apple56', 'apple@gmail.com', '0704194672', 'pesay')
        received_data = json.loads(register.data.decode())
        self.assertTrue(received_data['status'], 'fail')
        self.assertTrue(received_data['error_message'], 'A name should consist of only alphabetic characters')
        self.assertTrue(received_data['data'])
        self.assertTrue(register.content_type, 'application/json')
        self.assertEqual(register.status_code, 400)

    # def test_user_name_exists(self):
    #     """
    #     Test when the user name already exists
    #     :return:
    #     """
    #     self.register_user('Apple', 'apple@gmail.com', '0704194672', 'pesay')
    #     register = self.register_user('Apple', 'apple@gmail.com', '0704194672', 'pesay')
    #     response_data = json.loads(register.data.decode())
    #     self.assertTrue(response_data['status'], 'fail')
    #     self.assertTrue(response_data['error_message'], 'Username already taken')
    #     self.assertFalse(response_data['data'])
    #     self.assertTrue(register.content_type, 'application/json')
    #     self.assertEqual(register.status_code, 409)












