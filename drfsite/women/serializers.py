from rest_framework import serializers
from .models import Category, Women


class WomenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Women
        fields = ('id', 'name', 'surname', 'age', 'content', 'category')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
