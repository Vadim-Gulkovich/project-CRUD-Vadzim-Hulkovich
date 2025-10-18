from django.urls import path
from .views import BookList, BookDetail, BookAdd, BookUpdate, BookDelete

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('books/add/', BookAdd.as_view(), name='book-add'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
    path('books/<int:pk>/update/', BookUpdate.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', BookDelete.as_view(), name='book-delete'),
]