from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('register', register, name='register'),
    path('users', users, name='users'),
    path('login', login, name='login')
]
