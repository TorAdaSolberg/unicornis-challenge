#meeting/forms/meeting_creation.py
from django import forms
from django.forms import ModelForm
from meetings.models import Meeting
from organizations.models import Organization

class MeetingCreateForm(ModelForm):


    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user',None)
        super(MeetingCreateForm, self).__init__(*args, **kwargs)
        self.fields['organization'].queryset = Organization.objects.filter(
                                            members = self.user)


    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        information = cleaned_data.get('information')
        time_date = cleaned_data.get('time_date')


    class Meta:
        model = Meeting
        fields = [
            'organization',
            'title',
            'information',
            'time_date']
        labels = {
            'title': ('Tittel'),
            'information': ('Fyll inn innkallingsbrev'),
            'time_date': ('Sett en dato'),
        }

class EditMeeting(forms.Form):
    pass
