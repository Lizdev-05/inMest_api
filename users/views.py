from django.shortcuts import render

from users.serializers import UserSerializer
from .models import *
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view, permission_classes, action
from users.serializers import *
from rest_framework import status

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
    # USer authentication
        auth_user = authenticate(username=username, password=password)
        if auth_user:
            # Login User
            login(request, user)
            serializer = AuthSerializer(user, many=False)
            return Response({"Result": serializer.data })
        
        else:
            return Response({"detail": "Invalid credentials"}, status.HTTP_400_BAD_REQUEST)

    except IMUser.DoesNotExist:
        return Response({"Detail": "Username does not exist"}, status.HTTP_400_BAD_REQUEST)
    

