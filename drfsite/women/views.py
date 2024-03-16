from rest_framework.viewsets import ModelViewSet
from .models import Women, Category
from .serializers import WomenSerializer, CategorySerializer


class WomenViewSet(ModelViewSet):
    serializer_class = WomenSerializer
    queryset = Women.objects.all()


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
