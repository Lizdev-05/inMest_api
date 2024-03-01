from django.urls import path
from .views import *

 
urlpatterns = [
path('users/signup/', signup),
path('users/login/', user_login)
]