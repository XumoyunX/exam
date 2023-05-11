from django.shortcuts import render
 
from main.models import CategoriyaBook, Book
from rest_framework import viewsets, generics
from main.serializers import CategoriyaBookSerializer, BookSerializer


# class BookViewSet(viewsets.ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class =  CategoriyaBookSerializer




class CategoriyaBook(generics.ListCreateAPIView):
    queryset = CategoriyaBook.objects.all()
    serializer_class = CategoriyaBookSerializer




class Book(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer    


