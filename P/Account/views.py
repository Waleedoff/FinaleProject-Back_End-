from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken
from .serializer import UserRegisterSerializer
# from .models import User


# Create your views here.

@api_view(['POST'])
def register(request: Request):
    '''
    this method to allow user  register on this website 
    
    '''
    user_serializer = UserRegisterSerializer(data=request.data) # take userRegisterSerializer and convert to json .
    if user_serializer.is_valid():
        new_user = User.objects.create_user(**user_serializer.data)
        new_user.save()
        return Response({"msg": "created user successfuly"}, status=status.HTTP_200_OK)
    else:
        print(user_serializer.errors)
        return Response({"msg": "Couldn't create user"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login_user(request: Request):
     '''
    this method to allow user  Login on this website 
    
    '''
    if 'username' in request.data and 'password' in request.data:
        user = authenticate(request, username=request.data['username'], password=request.data['password'])
        if user is not None:
            # create the token , then give the token to the user in the response
            token = AccessToken.for_user(user)
            responseData = {
                "msg": "Your token is ready",
                "token": str(token)
            }
            return Response(responseData)

    return Response({"msg": "please provide your username & password"}, status=status.HTTP_401_UNAUTHORIZED)
