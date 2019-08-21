from django.contrib import admin
from .models import Organization, OrganizationMember

# Register your models here.
admin.site.register(OrganizationMember)
admin.site.register(Organization)
