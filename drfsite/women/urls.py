from django.urls import path, include
from .views import CategoryViewSet, WomenList, WomenDetail
from rest_framework import routers

r = routers.DefaultRouter()
r.register(r'category', CategoryViewSet)
app_name = 'women'

urlpatterns = [
    path('', include(r.urls)),
    path('women/', WomenList.as_view()),
    path('women/<pk>/', WomenDetail.as_view()),
]
