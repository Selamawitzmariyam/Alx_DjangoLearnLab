from django.urls import path
from .views import RegisterUserView, CustomAuthToken

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow'),
]
