from rest_framework import serializers
from rest_framework.serializers import Serializer
from todo.models import Todo
from django.utils import timezone
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="todo:users-detail")

    class Meta:
        model = User
        fields = ["url", "pk", 'username', 'first_name',
                  'last_name', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        username = validated_data['username']
        firstname = validated_data['first_name']
        lastname = validated_data['last_name']
        password = validated_data['password']
        email = validated_data['email']
        user = User(
            username=username, first_name=firstname, last_name=lastname, email=email)
        user.set_password(password)
        user.save()
        Token.objects.create(user=user)
        return user


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}


class TodoSerializer(serializers.ModelSerializer):
    cat = serializers.StringRelatedField(read_only=True)
    employee = serializers.ReadOnlyField(source="employee.username")

    class Meta:
        model = Todo
        fields = "__all__"

    def validate_start_time(self, value):
        if value < timezone.now():
            raise serializers.ValidationError(
                "The start time should be ahead of current time")
        return value

    def validate_end_time(self, value):
        if value < timezone.now():
            raise serializers.ValidationError(
                "The end time should be ahead of current time")
        return value
