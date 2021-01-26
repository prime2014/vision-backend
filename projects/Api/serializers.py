from rest_framework import serializers
from projects.models import Projects, ActionItems, Tasks
from django.contrib.auth.models import User
from todo.Api.serializers import UserSerializer
from profiles.Api.serializers import ProfileSerializer
from profiles.models import Profile
from datetime import datetime


class ProjectsSerializers(serializers.HyperlinkedModelSerializer):
    members = ProfileSerializer(instance=Profile.objects.all(), many=True)
    url = serializers.HyperlinkedIdentityField(
        view_name="projects:projects-detail")

    class Meta:
        model = Projects
        fields = ["url", "id", "title", "members"]


class TasksSerializers(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="projects:tasks-detail")
    action = serializers.PrimaryKeyRelatedField(
        queryset=ActionItems.objects.all(), many=False)
    assigned = serializers.HyperlinkedRelatedField(queryset=User.objects.all(),
                                                   view_name="todo:users-detail", many=True, required=False)
    watch = serializers.HyperlinkedRelatedField(queryset=User.objects.all(),
                                                view_name="todo:users-detail", many=True, required=False)
    due_date = serializers.DateTimeField(
        format="%a %b %d, %Y %H:%M %p", input_formats=["%d/%m/%Y %H:%M", ])

    class Meta:
        model = Tasks
        fields = ['assigned', 'url', 'pk', 'action',
                  'title', 'description', 'due_date', 'watch']

    # def update(self, instance, validated_data):
    #     instance.action = validated_data.get('action', instance.action)
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.due_date = validated_data.get('due_date', instance.due_date)
    #     instance.description = validated_data.get(
    #         'description', instance.description)
    #     instance.save()
    #     return instance


class AssignUserSerializer(TasksSerializers):
    class Meta:
        model = Tasks
        fields = ['assigned']


class AssignWatchSerializer(TasksSerializers):
    class Meta:
        model = Tasks
        fields = ['watch']


class ActionItemSerializer(serializers.HyperlinkedModelSerializer):
    project = serializers.HyperlinkedRelatedField(
        view_name="projects:projects-detail", queryset=Projects.objects.all())
    url = serializers.HyperlinkedIdentityField(
        view_name="projects:actionitems-detail")
    action_card = TasksSerializers(many=True, required=False)

    class Meta:
        model = ActionItems
        fields = ["url", "pk", "project", "title", "action_card"]
