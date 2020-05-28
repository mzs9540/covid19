from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import WorldCovidStats

from ..serializers import WorldStatsSerializer

WORLD_STATS_URL = reverse('stats:world_table_data')

data = {
    'country': 'USA',
    'total_case': 122.0,
    'new_case': 222.0,
    'total_recovered': 222.2,
    'active_case': 222.2,
    'cases_per_million': 222.2,
    'deaths_per_million': 222.2,
    'total_death': 222.2,
    'new_death': 222.2
}


def sample_world_stat(args):
    """Create and Return a sample news"""
    return WorldCovidStats.objects.create(**args)


class PublicStatsApiTest(TestCase):
    """Test the publicly available stats API"""

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_stats_list(self):
        """Test retrieving a list of News"""
        sample_world_stat(data)
        data['active_case'] = 111.1
        data['country'] = 'China'
        sample_world_stat(data)

        res = self.client.get(WORLD_STATS_URL)

        world_stat = WorldCovidStats.objects.all().order_by('-total_case')
        serializer = WorldStatsSerializer(world_stat, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)


class PrivateStatsTestApi(TestCase):
    """Test the privately available Stats API"""

    def setUp(self):
        self.client = APIClient()
        self.non_staff_user = get_user_model().objects.create_user(
            'nonstaff@gmail.com',
            '7777777@'
        )
        self.staff_user = get_user_model().objects.create_superuser(
            'staff@mzs.com',
            'testpass'
        )

    def test_create_stats_via_staff(self):
        """Test creating stats via staff"""
        self.client.force_authenticate(self.staff_user)

        response = self.client.post(WORLD_STATS_URL, data)

        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_create_news_via_non_staff(self):
        """Test creating News via non staff user"""
        self.client.force_authenticate(self.non_staff_user)

        res = self.client.post(WORLD_STATS_URL, data)

        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
