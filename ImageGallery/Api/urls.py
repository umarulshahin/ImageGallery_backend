from django.urls import path
from Authentication_app.views import *

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
urlpatterns = [
    path('token/',MyTokenobtainedPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/',TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/',SignUp,name='signup')
]
