from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view, authentication_classes, permission_classes


@api_view(['GET'])
@authentication_classes(authentication_classes=())
@permission_classes(permission_classes=())
def api_root(request, format=None):
    return Response({
        'login': reverse(viewname="todo:login", request=request, format=format),
        'users': reverse(viewname="todo:users-list", request=request, format=format),
        'categories': reverse(viewname="categories:categories-list", request=request, format=format),
        'todos': reverse(viewname="todo:todos-list", request=request, format=format),
        'projects': reverse(viewname="projects:projects-list", request=request, format=format),
        'action_item': reverse(viewname="projects:actionitems-list", request=request, format=format),
        'tasks': reverse(viewname="projects:tasks-list", request=request, format=format),
        'user_profiles': reverse(viewname="profiles:profiles-list", request=request, format=format)
    })
