from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Sex(models.Model):
    sex = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.sex

class Genre(models.Model):
    name_genre = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.name_genre

class Artist(models.Model):
    name_artist = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='artis/%Y/%m/%d')
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, blank=True, null=True)
    sex = models.ForeignKey(Sex, on_delete=models.SET_NULL, blank=True, null=True)
    music = models.JSONField(default=dict, blank=True)
    header_photo = models.ImageField(upload_to='artis/%Y/%m/%d')
    album = models.JSONField(default=dict, blank=True)

    def __str__(self):
        return self.name_artist
    class Meat:
        verbose_name = 'Артисты'