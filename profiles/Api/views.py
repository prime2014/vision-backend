from rest_framework.viewsets import ModelViewSet
from profiles.Api.serializers import ProfileSerializer
from profiles.models import Profile


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
