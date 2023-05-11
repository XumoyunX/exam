from django.urls import path

from main import views


urlpatterns = [
    path('categoriya_book/', views.CategoriyaBook.as_view()),
    path('book/<int:pk>/', views.Book.as_view()),

]
