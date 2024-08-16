from django.urls import path
from .views import CustomLoginView, CustomLogoutView, register 

                   

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
]

# list_books, LibraryDetailView 
# path('books/', list_books, name='list_books'),
# path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),