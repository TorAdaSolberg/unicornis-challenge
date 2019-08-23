from django.urls import path
from . import views

urlpatterns = [
    path('', views.OrganizationList.as_view(), name='organization_memberlist'),
    path('/<int:pk>', views.OrganizationDetail.as_view(), name='organization_member_detail'),
    path('create', views.OrganizationCreate.as_view(), name='organization_member_mcreate'),
    path('update/<int:pk>', views.OrganizationUpdate.as_view(), name='organization_member_update'),
    path('delete/<int:pk>', views.OrganizationDelete.as_view(), name='organization_member_delete'),
]
