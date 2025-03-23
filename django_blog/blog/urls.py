from django.urls import path
from django.contrib.auth import views as auth_views
from . import views 
from .views import search_posts 
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/comments/new/',  views.CommentNewView.as_view(), name='comment-new'),
    path('post/<int:post_id>/comments/', views.CommentListView.as_view(), name='comment-list'),
    path('post/<int:post_id>/comment/', views.add_comment, name='add-comment'),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='edit-comment'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='delete-comment'),
    path('search/', search_posts, name='search'),
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts-by-tag'),
]
