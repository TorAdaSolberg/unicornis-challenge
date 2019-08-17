""" Meeting Attendance Model

This model tracks metadata about a given users attendance of meetings.
My working hypothesis is that it would be beneficial to make this relate on
a many-to-one(read ForeignKey) relation to the Meeting model. As this will make
it possible to relate multiple users to a meeting. And a one to one relation to
an organizationmember.

I find that the most sensible way to relate a user to a meeting is by this attendace
relation.

TODO: write the model.

"""
from django.db import models
from users.models import OrganizationMember

class Attendance(models.Model):
    pass
