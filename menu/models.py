from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save
from django.core.urlresolvers import reverse

from .utils import unique_slug_generator
User = settings.AUTH_USER_MODEL


def upload_location(instance, filename):
    # filebase, extention = filename.split(".")
    print('filename', filename)
    name, extention = filename.split('.')
    print(name)
    print(extention)
    return "%s/%s" %(name, extention)


# Create your models here.
class ContactDetails(models.Model):
    owner           = models.ForeignKey(User) # class_instance.model_set.all()
    name            = models.CharField(max_length=120)
    relationship    = models.CharField(max_length=120, null=True, blank=False)
    # image = models.ImageField(verbose_name='self.name')
    timestamp       = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)
    slug            = models.SlugField(blank=True, null=True)
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    image           = models.ImageField(upload_to=upload_location,
                                        null=True, blank=True,
                                        width_field="width_field",
                                        height_field="height_field")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return f"/contact/{self.slug}"
        return reverse('menu:detail', kwargs={'slug': self.slug})

    def get_object(self):
        return self.get_object().name

    @property
    def title(self):
        return self.name


def cd_pre_save_receiver(sender, instance, *args, **kwargs):
    print('saving..')
    print(instance.timestamp)
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)


# def cd_post_save_receiver(sender, instance, created, *args, **kwargs):
#     print('saved')
#     print(instance.timestamp)


pre_save.connect(cd_pre_save_receiver, sender=ContactDetails)

# post_save.connect(cd_post_save_receiver, sender=ContactDetails)
