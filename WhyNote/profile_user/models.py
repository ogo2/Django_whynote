from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    about_me = models.TextField(blank=True)
    mail = models.EmailField(max_length=150)
    def get_absolute_url(self):
        return reversed('profile', kwargs={'username': self.user.username})

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
# class Users(models.Model):
#     mail = models.EmailField(max_length=150)
#     name = models.CharField(max_length=150)
#     about_me = models.TextField(blank=True)
#     date_of_birth = models.DateTimeField(auto_now_add=True)
#     sex = models.CharField(max_length=10)
#     photo = models.ImageField(upload_to='photos_user/%Y/%m/%d/')
#     country = models.CharField(max_length=150)
#     followers = models.IntegerField(blank=True, null=True)
#     sub = models.IntegerField(blank=True, null=True)
#     music = models.JSONField(default=dict, blank=True)
#
#
#     def __str__(self):
#         return self.name
#
