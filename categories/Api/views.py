from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from categories.models import Category
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from categories.Api.serializers import CategorySerializer
from rest_framework import status


class CategoryListset(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # def get(self, request, *args, **kwargs):
    #     serializer = CategorySerializer(Category.objects.all())
    #     return Response({'data': serializer.data}, status=status.HTTP_200_OK)


class CategoryDetailset(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
