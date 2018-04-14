from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
# from .utils import code_generator
from django.db.models.signals import pre_save


User = settings.AUTH_USER_MODEL


class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    name                =models.CharField(max_length=120)
    age                 =models.IntegerField(default=0)
    home_address        =models.CharField(max_length=300)
    phone               =models.IntegerField(default=0)
    hobbies             = models.CharField(max_length=400)
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    image           = models.ImageField(upload_to='icon/',
                                        verbose_name='profile',
                                        null=True, blank=True,
                                        width_field="width_field",
                                        height_field="height_field")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return f"/contact/{self.slug}"
        return reverse('profiles:profile', kwargs={'pk': self.object.pk})

    @property
    def title(self):
        return self.name
#
# # def post_save_user_receiver(sender, instance, created, *args, **kwargs):
# #     if created:
# #         profile, is_created = Profile.objects.get_or_create(user=instance)
# #         default_user_profile = Profile.objects.get_or_create(user__id=1)[0] #user__username=
# #         default_user_profile.followers.add(instance)
# #         #profile.followers.add(default_user_profile.user)
# #         #profile.followers.add(2)
# #
# #
# # post_save.connect(post_save_user_receiver, sender=User)

