from rest_framework import serializers
from .models import TeamMember

class RoleSerializer(serializers.Field):
    """Role mapper, returns role_type in text for get requests"""
    ROLES = {
        '0': 'regular',
        '1': 'admin'
    }

    def to_representation(self, role_type):
        return self.ROLES[role_type]        

    def to_internal_value(self, data):
        if self.ROLES.get(data):
           return data
        raise serializers.ValidationError("Incorrect Value")


class TeamMemberSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    role = RoleSerializer()

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = TeamMember
        fields = '__all__'

