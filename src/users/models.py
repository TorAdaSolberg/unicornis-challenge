# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):

    #just a random addition to see if i could create a user with a phone number
    phone = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.email


class OrganizationMember(models.Model):
    '''
    The OrganizationMember models purpose is to act as a relation between the
    organization and a given user.
    reasoning:
        - if one organization treats CustomUser as a many-to-many relation it
        would be easily accessible for the organization and opposite for the user,
        object, and vice-versa.
        - if both organization and CustomUser have many-to-many relations it would
        in theory be possible to query for an object from another organization by mistake. This is why a given user is related to an organization through
        a through_field in this model. And thus the organization --> user relation should
        never infringe upon another organization, and a user should still be able to have only one account.
    Other nifty abilities by doing this:
        - it will be possible to set a permissiongroup on the creation of the user.
    '''

    member = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    org = models.ForeignKey('Organization', on_delete=models.CASCADE)

    ALL_RIGHTS = 'AR'
    SOME_RIGHTS = 'SR'
    VIEW_RIGHTS = 'VR'
    REVOKED_RIGHTS = 'RR'
    RIGHTS_GROUP_CHOICES = [
        (ALL_RIGHTS, 'Manager'),
        (SOME_RIGHTS, 'BoardMember'),
        (VIEW_RIGHTS, 'Member'),
        (REVOKED_RIGHTS, 'Excluded')
    ]
    member_rights_group = models.CharField(
        max_length=2,
        choices=RIGHTS_GROUP_CHOICES,
        default=VIEW_RIGHTS,
    )


    def is_manager(self):
        return self.member_rights_group in (self.ALL_RIGHTS)

    def is_board_member(self):
        return self.member_rights_group in (self.ALL_RIGHTS, self.SOME_RIGHTS)

    def is_member(self):
        return self.member_rights_group in (self.ALL_RIGHTS, self.SOME_RIGHTS, self.VIEW_RIGHTS)



class Organization(models.Model):
    """
    The organization model is the relation spacing off different organizations running
    the service, with its relation through OrganizationMember to CustumUser it should
    in theory be able to be a way to grant closed off access to multiple chosen CustomUsers through the OrganizationMember model. This makes it possible for a
    user to be a part of multiple organizations, but limit the scope for all
    intra-organization querying to what is actually related to the Organization model.
    """

    name = models.CharField(max_length=30)
    org_nr = models.CharField(max_length=20)
    members = models.ManyToManyField(
        CustomUser,
        through='OrganizationMember',
        through_fields=('org', 'member')
    )
