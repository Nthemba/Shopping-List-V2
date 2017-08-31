"""
test_users.py
"""

import unittest

from app.users import User

class Testusers(unittest.TestCase):
    """
    tests for class User
    """
    def setUp(self):
        self.user = User()

    def tearDown(self):
        del self.user

    def test_registration_successful(self):
        """
        Tests if user can create account
        Args
            email, username, password, cpassword
        Pass criteria
            test passes if assertEqual is true
        """
        res = self.user.createuser("junenthemba@gmail.com", "njune", "qwert", "qwert")
        self.assertEqual(res, "Registration successful")

    def test_email_exists(self):
        """
        Tests if email given already exists
        Args
            email, username, password, cpassword
        Pass criteria
            test passes if assertEqual is true
        """
        self.user.createuser("junenthemba@gmail.com", "njune", "qwerty", "qwerty")
        res = self.user.createuser("junenthemba@gmail.com", "njune", "qwerty", "qwerty")
        self.assertEqual(res, "Email already exists.")

    def test_username_exists(self):
        """
        Tests if email given already exists
        Args
            email, username, password, cpassword
        Pass criteria
            test passes if assertEqual is true
        """
        self.user.createuser("junenthemba@gmail.com", "njune", "qwerty", "qwerty")
        res = self.user.createuser("liamkosgei@gmail.com", "njune", "qwerty", "qwerty")
        self.assertEqual(res, "Username already exists.")

    def test_passwords_match(self):
        """
        Tests if passwords match
        Args
            email, username, password, cpassword
        Pass criteria
            test passes if assertEqual is true
        """
        self.user.createuser("junenthemba@gmail.com", "njune", "qwerty", "qwerty")
        res = self.user.createuser("liamkosgei@gmail.com", "lune", "qwerty", "qwerty1")
        self.assertEqual(res, "Passwords do not match")
