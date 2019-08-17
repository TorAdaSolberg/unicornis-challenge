# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Organization, OrganizationMember

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = CustomUser
        fields = ('username', 'email')

class CreateOrganizationForm(forms.Form):

    class Meta(forms.Form):
        model = Organization
        fields = ('name', 'org_nr')

class CreateOrganizationMember(forms.Form):

    class Meta(forms.Form):
        model = OrganizationMember
        fields = ('user', 'organization')
