from django.urls import path
from .views import CategoryAPIView, WomenAPIView, WomenDetail, CategoryDetail

app_name = 'women'

urlpatterns = [
    path('women/', WomenAPIView.as_view(), name='women-list'),
    path('women/<pk>/', WomenDetail.as_view(), name='women-detail'),
    path('category/', CategoryAPIView.as_view(), name='category-list'),
    path('category/<pk>/', CategoryDetail.as_view(), name='category-detail'),
]
