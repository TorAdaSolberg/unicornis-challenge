from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save

# Create your models here.
class OrganizationMember(models.Model):

    #CHOICES:
    ALL_RIGHTS = 'AR'
    SOME_RIGHTS = 'SR'
    VIEW_RIGHTS = 'VR'
    REVOKED_RIGHTS = 'RR'
    CUSTOM_RIGHTS = 'CM'
    RIGHTS_GROUP_CHOICES = [
        (ALL_RIGHTS, 'Manager'),
        (SOME_RIGHTS, 'BoardMember'),
        (VIEW_RIGHTS, 'Member'),
        (REVOKED_RIGHTS, 'Excluded'),
        (CUSTOM_RIGHTS, 'Custom')
    ]

    #RELATION-FIELDS:
    member = models.ForeignKey(
                settings.AUTH_USER_MODEL,
                on_delete=models.CASCADE,)
    organization = models.ForeignKey('organizations.Organization',
                    on_delete=models.CASCADE,)
    #VALUE-FIELDS
    member_rights_group = models.CharField(
        max_length=2,
        choices=RIGHTS_GROUP_CHOICES,
        default=VIEW_RIGHTS,)
    bio = models.TextField(null=True, blank=True)


    #MANAGERS:
    objects = models.Manager()

    class Meta:
        verbose_name = 'organization_member'
        verbose_name_plural = 'organization_members'

    def __str__(self):
        return self.pk

    def is_manager(self):
        return self.member_rights_group in (self.ALL_RIGHTS)

    def is_board_member(self):
        return self.member_rights_group in (self.ALL_RIGHTS, self.SOME_RIGHTS)

    def is_member(self):
        return self.member_rights_group in (self.ALL_RIGHTS, self.SOME_RIGHTS, self.VIEW_RIGHTS)
