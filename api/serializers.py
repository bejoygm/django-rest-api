from rest_framework import serializers
from .models import TeamMember

class TeamMemberSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = TeamMember
        fields = ('first_name', 'last_name', 'phone_number', 'email')
        