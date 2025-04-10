from django.urls import path
from .views import RegisterUserView, CustomAuthToken

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', CustomAuthToken.as_view(), name='login'),
]