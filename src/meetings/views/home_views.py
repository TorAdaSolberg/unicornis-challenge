from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required()
def home_view(request, *args, **kwargs):
    return render(request, 'meeting/home.html')
