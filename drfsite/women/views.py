from rest_framework.generics import (
    CreateAPIView,
    ListCreateAPIView,
    DestroyAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
)
from .models import Women, Category
from .serializers import WomenSerializer, CategorySerializer


class WomenAPIView(ListCreateAPIView):
    serializer_class = WomenSerializer
    queryset = Women.objects.all()


class WomenDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = WomenSerializer
    queryset = Women.objects.all()


class CategoryAPIView(ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryDetail(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer