from django import views, forms
from meetings.forms import MeetingCreateForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='/accounts/login/')
def meeting_create(request):
    if request.method == 'POST':
        #Creating a form instance, populating with input data from the user.
        form = MeetingCreateForm(request.POST)

        #checking if fomr is valid
        if form.is_valid():
            #clean the data and save to database.
            form.clean()
            form.save()
    else:
        form = MeetingCreateForm(user=request.user)

    context = {
        'form' : form,
    }
    return render(request, 'meeting/meeting_create.html', context)

@login_required(login_url='accounts/login/')
class YourMeetings(views.View):
    pass
