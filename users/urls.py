from django.urls import path
from .views import *

 
urlpatterns = [
    path('users/signup/', signup),
    path('users/login/', user_login),
    path('users/forgot_password/', ForgotPasswordAPIView.as_view()),
    path('users/reset_password/', ResetPasswordAPIView.as_view()),
    path('users/change_password/', ChangePasswordAPIView(APIView)),
    path('users/me/', CurrentUserProfile.as_view()) ,
]
