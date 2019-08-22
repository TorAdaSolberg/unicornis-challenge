from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save

class Organization(models.Model):
    #CHOICES

    #RELATION-FIELDS:
    members = models.ManyToManyField(
         settings.AUTH_USER_MODEL,
         through='organization_members.OrganizationMember',
         through_fields=('organization', 'member'),
         blank=True,
         related_name='memberships',)

    #VALUE-FIELDS:
    name = models.CharField(max_length=30)
    org_nr = models.CharField(max_length=30)
    slug = models.SlugField(unique=True, blank=True)

    #MANAGERS:
    objects = models.Manager()

    class Meta:
        verbose_name = 'organization'
        verbose_name_plural = 'organizations'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('organization_details', kwargs={'slug': self.slug })

def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_post_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_reciever, sender='organizations.Organization')
