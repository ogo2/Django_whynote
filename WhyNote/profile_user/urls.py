from django.urls import path
from .views import *



urlpatterns = [
    path('profile/<str:username>/', profile2, name='profile'),
    path('registr/', RegisterUser.as_view(), name='registr'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),

]