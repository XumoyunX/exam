from rest_framework import routers, serializers, viewsets
from  main.models import CategoriyaBook, Book


class CategoriyaBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriyaBook
        fields = "__all__"




class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"        