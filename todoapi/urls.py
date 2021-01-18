from django.contrib import admin
from django.urls import path
from .views import api_root
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^login/', include('rest_framework.urls')),
    url(r'^$', api_root, name="root"),
    url(r'^tasks/', include('todo.urls')),
    url(r'cat/', include('categories.urls')),
    url(r'projects/', include('projects.urls')),
    url(r'user_profiles/', include('profiles.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
