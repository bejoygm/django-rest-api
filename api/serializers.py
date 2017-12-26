from rest_framework import serializers
from .models import TeamMember

class TeamMemberSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    role = serializers.SerializerMethodField()

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = TeamMember
        extra_kwargs = {"email": {"error_messages": {"required": "Give yourself a username"}}}
        fields = ('user_id', 'first_name', 'last_name', 'phone_number', 'email', 'role')

    # for human-readable value of role field
    def get_role(self, obj):
        return obj.get_role_display()