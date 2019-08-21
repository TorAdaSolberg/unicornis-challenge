from .models import Organization, OrganizationMember
from django.forms import ModelForm

class CreateOrganizationForm(ModelForm):

    # def clean_populate_save(self, request):
    #     self.clean()
    #     org=super(CreateOrganizationForm, self).save(commit=False)
    #     #org.owner=request.user #prøver å assigne eier av ting, blir knot
    #     org.save()


    def clean(self):
        cleaned_data = super().clean()
        self.name = cleaned_data.get('name')
        self.org_nr = cleaned_data.get('org_nr')


    class Meta:
        model = Organization
        fields = ('name', 'org_nr')

class CreateOrganizationMemberForm(ModelForm):

    class Meta:
        model = OrganizationMember
        fields = ('member', 'org')
