from rest_framework import serializers
from profiles.models import Profile
from django.contrib.auth.models import User
from todo.Api.serializers import UserSerializer
from rest_framework.request import Request


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="profiles:profiles-detail")
    user = UserSerializer(read_only=True, context={'request': Request})

    class Meta:
        model = Profile
        fields = ["url", "id", "user", "image", "career"]
