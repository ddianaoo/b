from rest_framework.generics import (
    CreateAPIView,
    ListCreateAPIView,
    DestroyAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
)
from .models import Women, Category
from .serializers import WomenSerializer, CategorySerializer


class WomenAPIView(ListAPIView):
    serializer_class = WomenSerializer
    queryset = Women.objects.all()


class CategoryAPIView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
