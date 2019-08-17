from django.db import models

class Document(models.Model):
    title     = models.CharField(max_length=120)
    owner     = models.ForeignKey("users.CustomUser",
                                on_delete=models.CASCADE,
                                null=True)
    issue   = models.ForeignKey("Issue",
                                on_delete=models.CASCADE)#dette er kanskje dumt om man vil ha en personlig document-store
