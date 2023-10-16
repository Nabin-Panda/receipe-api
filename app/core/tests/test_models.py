from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successfull(self):
        """Test creating a new user with an email is successfull"""
        email = "test@nabin.gmail.com"
        password = "nabin"
        user = get_user_model().objects.create_user(email=email, password=password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test checks if the email is getting normalized or not"""
        email = "test@nabin.gmail.CoM"
        password = "nabin"
        user = get_user_model().objects.create_user(email=email, password=password)
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            email = ""
            password = "nabin"
            get_user_model().objects.create_user(email=email, password=password)

    def test_create_new_superuser(self):
        """Test creating new super user"""
        user = get_user_model().objects.create_superuser(
            email="test@nabin.gmail.com", password="testing"
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
