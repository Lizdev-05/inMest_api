from django.urls import path
from .views import *
rom .views import (
    QueryListCreateView,
    QueryDetailView,
    ClassScheduleListCreateView,
    ClassScheduleDetailView,
    CheckInView,
)
 
urlpatterns = [
    path('users/signup/', signup),
    path('users/login/', user_login),
    path('users/forgot_password/', ForgotPasswordAPIView.as_view()),
    path('users/reset_password/', ResetPasswordAPIView.as_view()),
    path('users/change_password/', ChangePasswordAPIView.as_view()),
    path('users/me/', CurrentUserProfile.as_view()) ,
    path('queries/', QueryListCreateView.as_view(), name='query-list'),
    path('queries/<int:pk>/', QueryDetailView.as_view(), name='query-detail'),
    path('class-schedules/', ClassScheduleListCreateView.as_view(), name='class-schedule-list'),
    path('class-schedules/<int:pk>/', ClassScheduleDetailView.as_view(), name='class-schedule-detail'),
    path('check-in/', CheckInView.as_view(), name='check-in'),
]
