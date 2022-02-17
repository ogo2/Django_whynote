from django.urls import path

from .views import *



urlpatterns = [
    path('magazine_list/', list_magazine, name='magazine_list'),
    path('magazine_page/<str:share>', page_magazine, name='article_page'),
    path('add_article/', add_article, name='add_article'),

]