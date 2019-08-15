from django.shortcuts import render
from users import views
# Create your views here.
def index(request, *args, **kwargs):
    return render(request, 'pages/index.html')
