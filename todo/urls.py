from django.conf.urls import url
from rest_framework import urlpatterns
from todo.Api.views import TodoViewSet, LoginApiView, UserViewSet
from rest_framework.routers import DefaultRouter

app_name = "todo"

router = DefaultRouter()
router.register('todos', viewset=TodoViewSet, basename="todos")
router.register('users', viewset=UserViewSet, basename="users")

urlpatterns = [
    url(r'^api/login/$', LoginApiView.as_view(), name="login"),
]

urlpatterns += router.urls
