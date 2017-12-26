from django.urls import reverse
from django.test import TestCase
from .models import TeamMember
from .serializers import TeamMemberSerializer

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
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_teammember(self):
        teammember = TeamMember.objects.get()
        response = self.client.get(
            reverse('details',
                kwargs={'pk': teammember.user_id}), format="json"
        )
        serializer = TeamMemberSerializer(teammember)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_api_can_update_teammember(self):
        teammember = TeamMember.objects.get()
        update_teammember = {'first_name': 'Transformer'}
        response = self.client.put(
            reverse('details', kwargs={'pk': teammember.user_id}),
            update_teammember, format='json'
        )
        self.assertEqual(response.data['first_name'], update_teammember['first_name'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_delete_teammember(self):
        """Test the api can delete a teammember."""
        teammember = TeamMember.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': teammember.user_id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)



