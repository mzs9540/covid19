from datetime import date

from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models


def sample_user(email='test@mzs.com', password='pssword123'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_succesful(self):
        """Test Creating new user with an email is successful"""
        email = 'test@mzs.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the new user is Normalized"""
        email = 'test@Mzs.com'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'Test123')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@mzs.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_covid19_news_str(self):
        """Test the Covid News string representation"""
        news = models.CovidNews.objects.create(
            title='Chicken Popcorn',
            href='mzs.com',
            date=date.today()
        )

        self.assertEqual(str(news), news.title)
