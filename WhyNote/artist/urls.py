from django.urls import path
from .views import *



urlpatterns = [
    path('artist_list/', artist_list, name='artist_list'),
    path('artist_page/<str:artist_name>/', artist_page, name='artist_page'),
]