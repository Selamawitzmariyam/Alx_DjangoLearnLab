from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class Register(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')  # Redirect to login after signup
    template_name = 'registration/register.html'
