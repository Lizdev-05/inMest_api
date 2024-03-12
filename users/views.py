from django.shortcuts import render

from users.serializers import UserSerializer
from .models import *
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes, action
from users.serializers import *
from rest_framework import status
from inMest_api.utils import *
from .models import IMUser

# Create your views here.

# @api_view(['POST'])
# @permission_classes([AllowAny])
# def signup(request):
#     username = request.data.get["username"]
#     first_name = request.data.get["first_name"]
#     last_name = request.data.get["last_name"]
#     phone_number= request.data.get["phone_number"]
#     password = request.data.get["password"]

#     new_user = IMUser.objects.create(
#         username=username,
#         first_name=first_name,
#         last_name=last_name,
#         phone_number=phone_number
#         )
#     new_user.set_password(password)
#     new_user.save()
#     new_user.generate_auth_token()
#     serializer = UserSerializer(new_user, many=False)
#     return Response({"Message": "Account created successfully", "result": serializer.data})

@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    username = request.data.get("username")
    first_name = request.data.get("first_name")
    last_name = request.data.get("last_name")
    phone_number= request.data.get("phone_number")
    password = request.data.get("password")

    new_user = IMUser.objects.create(
        username=username,
        first_name=first_name,
        last_name=last_name,
        phone_number=phone_number
        )
    new_user.set_password(password)
    new_user.save()
    # new_user.generate_user_token()
    serializer = AuthSerializer(new_user, many=False)
    return Response({"Message": "Account created successfully", "result": serializer.data})
@api_view(["POST"])
@permission_classes([AllowAny])
def user_login(request):
    # Receive inputs/data from client and validate inputs
    username = request.data.get("username")
    password = request.data.get("password")

    if not username or not password:
        return Response({"Detail": "Kindly input your username and password"}, status.HTTP_400_BAD_REQUEST)

    # Check user existence
    try:
        user = IMUser.objects.get(username = username)
# Ass
           # Check if the user is active
        if not user.is_active:
            return Response({"Detail": "Your account is inactive"}, status.HTTP_403_FORBIDDEN)
        
    # USer authentication
        auth_user = authenticate(username=username, password=password)
        if auth_user:
            # ass
             # Reset temporal_login_fail if login is successful
            user.temporal_login_fail = 0
            user.save()
            # Login User
            login(request, user)
            serializer = AuthSerializer(user, many=False)
            return Response({"Result": serializer.data })
        
        else:
            # Ass
              # Increment temporal_login_fail if login fails
            user.temporal_login_fail += 1
            user.save()
            return Response({"detail": "Invalid credentials"}, status.HTTP_400_BAD_REQUEST)

    except IMUser.DoesNotExist:
        return Response({"Detail": "Username does not exist"}, status.HTTP_400_BAD_REQUEST)
    


class ForgotPasswordAPIView(APIView):
    permission_classes=[AllowAny]

    def post(self, request):
        # receive the username or email
        username = request.data.get("username")
        if not username:
            return generate_400_response("Please provide a valid udername")
        
        # Check if user exists
        try:
            user = IMUser.objects.get(username = username)
            otp_code = generate_unique_code()
            # Send otp
            user.unique_code = otp_code
            user.save()
            # send email or sms at this point
            
            # respond to tge user
            return Response({"Detail": "Please check your email for an OTP"}, status.HTTP_200_OK)
            
        except IMUser.DoesNotExist:
            return generate_400_response("Username does not exist")
        


class ResetPasswordAPIView(APIView):
    permission_classes=[AllowAny]
    def post(self, request):
        username = request.data.get("username")
        unique_code = request.data.get("unique_code")
        new_password = request.data.get("new_password")

        if not (username and unique_code and new_password):
            return Response({"detail": "Please provide username, unique code, and new password"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = IMUser.objects.get(username=username, unique_code=unique_code)
            user.set_password(new_password)
            user.save()
            return Response({"detail": "Password reset successfully"}, status=status.HTTP_200_OK)
        except IMUser.DoesNotExist:
            return Response({"detail": "Invalid username or unique code"}, status=status.HTTP_400_BAD_REQUEST)
        
class CurrentUserProfile(APIView):
    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)


        
class ChangePasswordAPIView(APIView):
     def post(self, request):
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")

        if not (old_password and new_password):
            return Response({"detail": "Please provide old password and new password"}, status=status.HTTP_400_BAD_REQUEST)

        user = request.user
        if not user.check_password(old_password):
            return Response({"detail": "Incorrect old password"}, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(new_password)
        user.save()
        return Response({"detail": "Password changed successfully"}, status=status.HTTP_200_OK)

