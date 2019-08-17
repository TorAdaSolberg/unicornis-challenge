# meeting/forms.py
from django import forms

class MeetingCreationForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)
    group =
    cc_myself = forms.BooleanField(required=False)

class MeetingChangeForm(forms.Form):

    class Meta():
        model = CustomUser
        fields = ('username', 'email')
