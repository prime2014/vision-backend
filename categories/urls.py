from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from categories.Api.views import CategoryListset, CategoryDetailset

app_name = "categories"


urlpatterns = [
    url(r'^categories/$', CategoryListset.as_view(), name="categories-list"),
    url(r'^categories/(?P<pk>[0-9]+)/$',
        CategoryDetailset.as_view(), name="category-detail"),
]
