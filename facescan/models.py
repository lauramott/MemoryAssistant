from django.db import models
from django.conf import settings
# Create your models here.
from django.core.urlresolvers import reverse
from menu.models import ContactDetails
from django.db.models.signals import pre_save
from django.utils.text import slugify
from .utils import unique_slug_generator


def upload_location(instance, filename):
    filebase, extention = filename.split(".")
    return "%s/%s.%s" %(instance.id, instance.id, extention)


class Item(models.Model):
    # associations
    user        = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contact     = models.ForeignKey(ContactDetails)
    # image stuff
    slug        = models.SlugField(unique=True, blank=True, null=True)
    name        = models.CharField(max_length=120)
    public      = models.BooleanField(default=True)
    timestamp       = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    image           = models.ImageField(upload_to=upload_location,
                                        null=True, blank=True,
                                        width_field="width_field",
                                        height_field="height_field")

    def __str__(self):
        print(self.user)
        return str(self.user)

    def get_absolute_url(self):
        # return f"/contact/{self.slug}"
        return reverse('facescan:detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-updated', '-timestamp']
        # item.objects.all() it will return most recent item updated forst


def item_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(item_pre_save_receiver, sender=Item)
