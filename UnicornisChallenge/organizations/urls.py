from django.urls import path, redirect
from . import views

urlpatterns = [
    path(),
    path('Organizations', views.OrganizationList.as_view(), name='Organization_list'),
    path('Organization/<int:pk>', views.OrganizationDetail.as_view(), name='Organization_detail'),
    path('create', views.OrganizationCreate.as_view(), name='Organization_create'),
    path('update/<int:pk>', views.OrganizationUpdate.as_view(), name='Organization_update'),
    path('delete/<int:pk>', views.OrganizationDelete.as_view(), name='Organization_delete'),
]
