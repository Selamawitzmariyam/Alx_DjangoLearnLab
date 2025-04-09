from django.urls import path, include
from .views import Register
from django.views.generic import TemplateView

urlpatterns = [
  
    path('login',LoginView.as_view(template_name='login.html',name ='login'),
    path('login',LogoutView.as_view(template_name='logout.html',name ='login'),
    path('signup/',views.register, name='register'),    # Custom registration
    path('accounts/register/',                                
         TemplateView.as_view(template_name='relationship_app/register.html'),
         name='profile'),
]
