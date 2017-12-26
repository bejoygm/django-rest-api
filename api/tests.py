from django.urls import reverse
from django.test import TestCase
from .models import TeamMember

from rest_framework.test import APIClient
from rest_framework import status

class ModelTestCase(TestCase):
    """This class defines the test suite for the teammember model."""

    def setUp(self):
        """Defines the test client and other test variables."""
        self.teammember_first_name = "Alpha"
        self.teammember = TeamMember(first_name=self.teammember_first_name)

    def test_model_can_create_a_teammember(self):
        old_count = TeamMember.objects.count()
        self.teammember.save()
        new_count = TeamMember.objects.count()
        self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        self.client = APIClient()
        self.teammember_data = {
            'first_name': 'Alpha',
            'last_name': 'Omega',
            'phone_number': '+999999999',
            'email': 'a@a.com',
        }
        self.response = self.client.post(
            reverse('create'),
            self.teammember_data,
            format="json"
        )

    def test_api_can_create_a_teammember(self):
        self.assertNotEqual(self.response.status_code, status.HTTP_201_CREATED)

