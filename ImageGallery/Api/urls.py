from django.urls import path
from Authentication_app.views import *
from Main_app.views import *

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
urlpatterns = [
    path('token/',MyTokenobtainedPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/',TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/',SignUp,name='signup'),
    path('forgetPassword/',Forget_password,name='forgetPassword'),
    path('otp_validation/',OTP_validation,name='otp_validation'),
    path('newpassword/',NewPassword,name='newpassword'),
    path('image_upload/',Image_Upload,name='image_upload'),
    path('getimage/',Get_Image,name='getimage'),
    path('imageorder/',Image_Order,name='imageorder'),
    path('deleteimage/',Delete_Image,name='deleteimage')
    
    
]
