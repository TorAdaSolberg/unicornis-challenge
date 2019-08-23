from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from .models import Organization

# CRUD views
class OrganizationList(ListView):
    model = Organization

class OrganizationDetail(DetailView):
    model = Organization

class OrganizationCreate(CreateView):
    model = Organization

class OrganizationUpdate(UpdateView):
    model = Organization

class OrganizationDelete(DeleteView):
    model = Organization
