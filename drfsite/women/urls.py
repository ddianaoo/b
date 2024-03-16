from django.urls import path, include
from .views import CategoryViewSet, WomenViewSet
from rest_framework import routers

r = routers.DefaultRouter()
r.register(r'category', CategoryViewSet)
r.register(r'women', WomenViewSet, basename='women')
app_name = 'women'

urlpatterns = [
    path('', include(r.urls)),
]
