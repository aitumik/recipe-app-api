from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models

def sample_user(email="test@deveint.com", password="testing"):
    """Create a sample user"""
    return get_user_model().objects.create_user(email,password)


class ModelTest(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successfull"""
        email = "nathan@sitepuller.com"
        password = "testing"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user normalized"""
        email = 'test@DEVEINT.COM'
        user = get_user_model().objects.create_user(email, 'testing123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "testing123")

    def test_create_new_superuser(self):
        """Test creation of a new superuser"""
        user = get_user_model().objects.create_superuser(
            'nathan@deveint.com',
            'testing'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )

        self.assertEqual(str(tag), tag.name)
