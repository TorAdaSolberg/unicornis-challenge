from django.db import models
# Create your models here.
"""
The meeting model is the common relation between all models used when creating a meeting.
"""
class Meeting(models.Model):
    title = models.CharField(max_length=120)
    summary = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(
        'users.CustomUser',
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return self.title


class Issue(models.Model):
    title       = models.CharField(max_length=120)
    meeting     = models.ForeignKey('Meeting', on_delete=models.CASCADE)
    owner = models.ForeignKey(
        'users.CustomUser',
        on_delete=models.CASCADE,
        null=True)
    abstract    = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

class Document(models.Model):
    title     = models.CharField(max_length=120)
    owner     = models.ForeignKey("users.CustomUser",
                                on_delete=models.CASCADE,
                                null=True)
    issue   = models.ForeignKey("Issue",
                                on_delete=models.CASCADE)#dette er kanskje dumt om man vil ha en personlig document-store
