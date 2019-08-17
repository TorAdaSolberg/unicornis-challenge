from django.db import models
# Create your models here.

class Meeting(models.Model):
    """ This is a model containing information about meetings. Recursively it is a the common relation between all information needed to represent a meeting in the meeting application. The idea is that if one creates a meeting in the front-end view, one should be able to create issues, set time and date, location and so on and so forth.

    attributes:
        title: String
            Meeting title
        information: TextField
            contains a summary of the meeting, invitation text, whatever the user wants to inform about. Maybe, havent really figured out how i want this to work yet.
        owner: User
            relation: many to one
            Owner of meeting object, it should by default be made to be the creator.
            Although it seems like a good idea to make it a ManyToManyField to support multiple editors,
            multiple editors might also be implemented as another ManyToManyField with permissions
            TODO: make infrastructure to make sure Meeting relations get an owner
    """
    title = models.CharField(max_length=120)
    information = models.TextField(blank=True, null=True)
    organization = models.ForeignKey(
        'users.Organization',
        on_delete=models.CASCADE
    )
    owner = models.ForeignKey(
        'users.CustomUser',
        on_delete=models.SET_NULL,
        null=True
    )
    time_date = models.DateTimeField()

    def __str__(self):
        return self.title
