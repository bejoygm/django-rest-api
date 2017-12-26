from rest_framework import generics
from .serializers import TeamMemberSerializer
from .models import TeamMember

class CreateView(generics.ListCreateAPIView):
    """Create behaviour of rest api"""
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist"""
        serializer.save()

    