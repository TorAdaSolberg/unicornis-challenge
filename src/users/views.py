# users/views.py
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import render
from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def login_view(request, *args, **kwargs):
    render(request, 'login.html')
