from django.urls import path
from .views import *

urlpatterns = [
    path('', perform_registeration, name='register'),
    path('login/', perform_login, name='login'),
    path('logout/', logoutUser, name='logout'),
]