from django.urls import path, include
from .views import SignUpView
from django.views.generic import TemplateView

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),  # Django's built-in auth routes

    path('signup/', SignUpView.as_view(), name='signup'),    # Custom registration

]
