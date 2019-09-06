from django.urls import path

from . import views

urlpatterns = [
    path('', views.AppView.as_view()),
    path('auth', views.AuthView.as_view()),
    path('books', views.BooksView.as_view()),
]
