from rest_framework import serializers
from rest_framework.serializers import Serializer

from categories.models import Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name', 'tagline']
