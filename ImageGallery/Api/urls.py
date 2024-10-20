from django.urls import path
from Authentication_app.views import *


urlpatterns = [
    path('signup/',SignUp,name='signup')
]
