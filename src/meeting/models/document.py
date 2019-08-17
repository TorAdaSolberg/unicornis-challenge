from django.db import models


class Document(models.Model):
    '''
    The document model, is a model that makes it possible for users to either upload or
    link to a document. How it should relate in the system:
    - It should exist within a users own space, visible only to that user. Except
    if it is shared to a space, i.e. a meeting. This model class might be made abstract
    and exist as either a documentlink model, or a documentfile model.
    - I dont believe it actually needs any other relation than to user, because it can
    be extrapolated in the view-layer, which also makes querying for it quite simple and efficient.

    TODO: create infrastructure to store documentfile which is why the doc_link
    attribute is commented out.
    '''
    title     = models.CharField(max_length=120)
    owner     = models.ForeignKey("users.CustomUser",
                                on_delete=models.CASCADE,
                                null=True)
    #doc_link = models.FileField()
