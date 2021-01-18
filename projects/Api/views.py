from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from projects.models import Projects, ActionItems, Tasks
from projects.Api.serializers import(
    ProjectsSerializers,
    ActionItemSerializer,
    TasksSerializers,
    ShiftTasksSerializers
)
from django.utils import timezone
from rest_framework.response import Response
from rest_framework import exceptions
import time
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework import status


class ProjectViewSet(ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['members__user__username']


class ActionItemsViewSet(ModelViewSet):
    queryset = ActionItems.objects.all()
    serializer_class = ActionItemSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['project__id']


class TasksViewSet(ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['action__title']

    def create(self, request, *args, **kwargs):
        time.sleep(5)
        serializer = TasksSerializers(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @action(detail=True, methods=['PUT', 'GET'])
    def next(self, request, *args, **kwargs):
        """Concrete action for updating a single instance of task"""
        pk = kwargs['pk']
        if request.method == "PUT":
            choice = Tasks.objects.get(pk=pk)
            choice.action = ActionItems.objects.get(pk=request.data['action'])
            choice.save()
            serializer = TasksSerializers(
                choice, context={'request': request})
            return Response(serializer.data)
        elif request.method == "GET":
            choice = Tasks.objects.get(pk=pk)
            serializers = TasksSerializers(
                choice, context={'request': request})
            return Response(serializers.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['PUT', 'GET'])
    def previous(self, request, *args, **kwargs):
        """Concrete action for updating a single instance of task"""
        pk = kwargs['pk']
        if request.method == "PUT":
            choice = Tasks.objects.get(pk=pk)
            choice.action = ActionItems.objects.get(pk=request.data['action'])
            choice.save()
            serializer = TasksSerializers(
                choice, context={'request': request})
            return Response(serializer.data)
        elif request.method == "GET":
            choice = Tasks.objects.get(pk=pk)
            serializers = TasksSerializers(
                choice, context={'request': request})
            return Response(serializers.data, status=status.HTTP_200_OK)
