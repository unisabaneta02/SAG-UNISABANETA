from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.get_books, name='get_books'),
    path('books/', views.add_book, name='add_book'),
    path('books/<int:book_id>/', views.delete_book, name='delete_book'),
    path('', views.api_root, name='api_root'),  # Rut para /api/
]
