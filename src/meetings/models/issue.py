from django.db import models
# Create your models here.
from organizations.models import Organization, OrganizationMember

class Issue(models.Model):
    """
    The Issue model as a model handling issues in the meeting scheduler app.
    The working idea is that it is primarily going to exist as a ForeignKey to
    organization.

    My idea:
    - if it exists as a many-to-one relation with organization the system will
    be able to link the issue to several meetings or other views where it will
    be practical and wished for.
    - Optional?/required? field owner will make it possible to have concurrency
    in issue handling i.e. after a new board have been elected from a general
    assembly.
    - Seems possible. Maybe even smart.

    """
    title = models.CharField(max_length=120)

    organization = models.ForeignKey(
        Organization,
        on_delete = models.CASCADE
        )

    owner = models.ForeignKey(
        OrganizationMember,
        on_delete=models.SET_NULL,
        null=True)
    abstract        = models.TextField(blank=True, null=True)
    IS_ACTIVE = models.BooleanField(default=True)


    def __str__(self):
        return self.title
