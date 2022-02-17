from django.contrib import admin

from .models import *

admin.site.register(Genre_article)
admin.site.register(article)
admin.site.register(Comment)
admin.site.register(Likes)
