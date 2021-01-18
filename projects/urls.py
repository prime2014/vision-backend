from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from projects.Api.views import(
    ProjectViewSet,
    ActionItemsViewSet,
    TasksViewSet
)

app_name = "projects"

router = DefaultRouter()

router.register('projects', viewset=ProjectViewSet)
router.register('actionitems', viewset=ActionItemsViewSet)
router.register('tasks', viewset=TasksViewSet)


urlpatterns = [

]

urlpatterns += router.urls
