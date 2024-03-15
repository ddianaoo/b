from django.urls import path
from .views import CategoryAPIView, WomenAPIView

app_name = 'women'

urlpatterns = [
    path('women/', WomenAPIView.as_view()),
    path('category/', CategoryAPIView.as_view()),
]
