from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from .models import OrganizationMember

# CRUD views
class OrganizationList(ListView):
    model = OrganizationMember

class OrganizationDetail(DetailView):
    model = OrganizationMember

class OrganizationCreate(CreateView):
    model = OrganizationMember

class OrganizationUpdate(UpdateView):
    model = OrganizationMember

class OrganizationDelete(DeleteView):
    model = OrganizationMember
