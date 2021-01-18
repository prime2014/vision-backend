from rest_framework import filters
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from todo.Api.serializers import(
    TodoSerializer,
    LoginSerializer,
    UserSerializer
)
from todo.models import Todo
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class LoginApiView(APIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            return Response({"user": user.username, "token": user.auth_token.key})
        else:
            return Response({'error': 'Wrong credentials'}, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TodoViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['employee__username', 'status']

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(employee=self.request.user)
        else:
            raise AuthenticationFailed()
