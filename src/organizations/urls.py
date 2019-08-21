#organization/models.py
from django.urls import path, include

from .views import OrganizationCreateView, organization_home_view

urlpatterns = [
    path('create/', OrganizationCreateView.as_view(), name='create_org'),
    path('home/', organization_home_view, name='home'),
]
