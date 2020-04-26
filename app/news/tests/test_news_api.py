from datetime import datetime

from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import CovidNews

from news.serializers import WhoNewsSerializer

NEWS_URL = reverse('news:covidnews-list')


def sample_news(title='News',
                href='test.com',
                date=datetime.today().date()):
    """Create and Return a sample news"""
    return CovidNews.objects.create(title=title,
                                    href=href,
                                    date=date)


def detail_url(news_id):
    """return a details url"""
    return reverse('news:covidnews-detail', args=[news_id])


class PublicNewsApiTest(TestCase):
    """Test the publicly available news API"""

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_news_list(self):
        """Test retrieving a list of News"""
        sample_news(
            title='Covid1',
            href='test1.com',
            date=datetime.today().date())
        sample_news(
            title='Covid2',
            href='test2.com',
            date=datetime.today().date())

        res = self.client.get(NEWS_URL)

        news = CovidNews.objects.all().order_by('-date')
        serializer = WhoNewsSerializer(news, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)


class PrivateNewsTestApi(TestCase):
    """Test the privately available API"""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'test1@mzs.com',
            '786786786@'
        )
        self.user_admin = get_user_model().objects.create_superuser(
            'test@mzs.com',
            'testpass'
        )

    def test_create_news_via_staff(self):
        """Test creating News"""
        self.client.force_authenticate(self.user_admin)
        payload = {
            'title': 'Test news via staff user',
            'href': 'mzs.com',
            'date': datetime.today().date(),
        }
        res = self.client.post(NEWS_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        news = CovidNews.objects.get(id=res.data['id'])
        for key in payload.keys():
            self.assertEqual(payload[key], getattr(news, key))

    def test_create_news_via_non_staff(self):
        """Test creating News via non staff user"""
        self.client.force_authenticate(self.user)
        payload = {
            'title': 'Test News Via non staff User',
            'href': 'mzs.com',
            'date': datetime.today().date(),
        }
        res = self.client.post(NEWS_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
