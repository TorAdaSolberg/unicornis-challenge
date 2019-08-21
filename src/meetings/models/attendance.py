""" Meeting Attendance Model

This model is a join table between the Meeting model and the OrganizationMember model.
It is used to track attendance to meetings and contains three fields:
    member: a single member of type OrganizationMember
    meeting: a single meeting.
    attendance: BooleanField, True = member was at meeting

I find that the most sensible way to relate a user to a meeting is by this attendace
relation. Because that will make it really easy to create a view serving us for
instance attendees with voting rights or attendees that may edit issues or upload
documents.

TODO: write the model.

"""
from django.db import models
from organizations.models import OrganizationMember
from . import Meeting

class Attendance(models.Model):
    #if a member is deleted, set null, there was someone there.
    member = models.ForeignKey(
            OrganizationMember,
            on_delete=models.SET_NULL,
            null=True
    )
    #if a meeting is deleted, delete this because it is not necesseary to track unless there is a meeting to track attendance for.
    meeting = models.ForeignKey(
            Meeting,
            on_delete=models.CASCADE
    )
    attendance = models.BooleanField()
