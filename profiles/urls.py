from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from profiles.Api.views import ProfileViewSet

app_name = "profiles"

router = DefaultRouter()
router.register('profiles', viewset=ProfileViewSet, basename="profiles")


urlpatterns = [

]

urlpatterns += router.urls
