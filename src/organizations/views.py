#pardon my messy imports, not really sure what i am doing here

from django.shortcuts import render, redirect
from django import views
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Organization, OrganizationMember
from.forms import CreateOrganizationForm
from .utils import UserOrgs
# Create your views here.
@login_required()
def organization_home_view(request, *args, **kwargs):
    context = {
        'organizations': UserOrgs(request),
        'home_active' : 'active'
    }
    print(context)
    return render(request, 'organizations/home.html', context)

class OrganizationCreateView(LoginRequiredMixin, views.View):
    form_class = CreateOrganizationForm
    template_name = 'organizations/create_organization.html'
    success_url = reverse_lazy('home')

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.clean_populate_save(request)
            return redirect(reverse_lazy('home'))
        return redirect(request, )



    class Meta:
        model = Organization
        fields = [
            'name',
            'org_nr',]
        labels = {
            'name': ('Name'),
            'org_nr': ('Organization Number')
        }
