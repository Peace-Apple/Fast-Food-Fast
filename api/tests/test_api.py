"""
Tests module
"""
from flask import json

from unittest import TestCase

from run import APP

class TestFastFoodFast(TestCase):
    """
       Tests run for the api
       """

    def setUp(self):
        self.app = APP
        self.client = self.app.test_client

    def register_user(self, user_name=None, email=None, phone_number=None, password=None, user_type=None):
        return self.client().post(
            '/api/v2/auth/signup/',
            data=json.dumps(dict(
                user_name=user_name,
                email=email,
                contact=phone_number,
                password=password,
                user_type=user_type
            )),
            content_type="application/json"
        )

    def test_missing_fields_during_signup(self):
        """
        Test for missing fields during user registration
        :return:
        """
        register = self.client().post(
            '/api/v2/auth/signup/',
            data=json.dumps(dict(
                user_name='Acio',
                email='apple@gmail.com',
                phone_number='0789023564',
                password='mylife',
            )),
            content_type="application/json"
        )
        response_data = json.loads(self.register_user.data.decode())
        self.assertTrue(response_data['status'] == "fail")
        self.assertTrue(response_data['error_message'] == "some of these fields are missing")
        self.assertTrue(response_data['data'])
        self.assertTrue(register.content_type == "application/json")
        self.assertEqual(register.status_code, 400)

    def test_invalid_data_type(self):
        """
        Test user registration with invalid data-type
        :return:
        """
        register = self.register_user(5224524, 'acio@gmail.com', '0704252625', 'lifeisgood', 'admin')
        received_data = json.loads(register.data.decode())
        self.assertTrue(received_data['status'] == 'fail')
        self.assertTrue(received_data['error_message'] == 'Only string data type supported')
        self.assertFalse(received_data['data'])
        self.assertTrue(register.content_type == "application/json")
        self.assertEqual(register.status_code, 400)

    def test_empty_fields_during_signup(self):
        """
        Test for empty fields during user registration
        :return:
        """
        register = self.register_user(' ', 'acio@gmail.com', '0709876542', 'myfaith', 'admin')
        response_data = json.loads(register.data.decode())
        self.assertTrue(response_data['status'] == "fail")
        self.assertTrue(response_data['error_message'] == "some of these fields have empty/no values")
        self.assertTrue(response_data['data'])
        self.assertTrue(register.content_type == "application/json")
        self.assertEqual(register.status_code, 400)

    def test_invalid_email_registration(self):
        """
        Test for registration with invalid email
        :return:
        """
        register = self.register_user('Arnold', 'acio@gmail', '0706180672', 'persevere', 'admin')
        response_data = json.loads(register.data.decode())
        self.assertTrue(response_data['status'] == "fail")
        self.assertTrue(response_data['error_message'])
        self.assertTrue(response_data['data'])
        self.assertTrue(register.content_type == "application/json")
        self.assertEqual(register.status_code, 400)

    def test_invalid_phone_number(self):
        """
        testing invalid phone_number
        :return:
        """
        register = self.register_user('Apple', 'acire@gmail.com', '0706180', 'lovely', 'admin')
        data = json.loads(register.data.decode())
        self.assertEqual(register.status_code, 400)
        self.assertIn("error_message", data)
        self.assertTrue(data['error_message'])

    def test_invalid_user_name(self):
        """
        testing invalid username
        :return:
        """
        register = self.register_user('acio234', 'acire@gmail.com', '0704195673', 'itwillend', 'admin')
        data = json.loads(register.data.decode())
        self.assertIn("error_message", data)
        self.assertFalse(data['data'])
        self.assertTrue(data['error_message'])
        self.assertEqual(register.status_code, 400)
        self.assertTrue(register.content_type, 'application/json')

    def test_user_name_exists(self):
        """
        Test when the user name already exists
        :return:
        """
        self.register_user('Acio', 'acio@gmail.com', '0704194672', 'trustit', 'admin')
        register = self.register_user('Acio', 'acio@gmail.com', '0704194672', 'trustit', 'admin')
        response_data = json.loads(register.data.decode())
        self.assertTrue(response_data['status'] == "fail")
        self.assertTrue(response_data['error_message'] == "Username already taken")
        self.assertFalse(response_data['data'])
        self.assertTrue(register.content_type == "application/json")
        self.assertEqual(register.status_code, 409)












