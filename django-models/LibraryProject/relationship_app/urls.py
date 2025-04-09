from .views import list_books
from django.urls import path
from .views import book_list, LibraryDetailView ,SignupView # Import your views
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    path('books/', book_list, name='book_list'),  
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/',LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',LogoutView.as_view(template_name='logout.html'),name='logout'),
    path('register/',SignupView.as_view(template_name='register.html'),name="register")
]
