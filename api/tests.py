from django.test import TestCase
from .models import TeamMember

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

