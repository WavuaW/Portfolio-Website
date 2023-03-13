from django.shortcuts import render
from user.models import User
from user.serializer import UserSerializer
from rest_framework.response import Response
from django.contrib import messages
from rest_framework.generics import GenericAPIView
from django.contrib.auth import authenticate, login
from rest_framework import status
from user.token import generate_auth_token



# Create your views here.

class RegisterView(GenericAPIView):
    """
        description - register a user
    """

    serializer_class = UserSerializer

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            message = messages.success(request, "Account created successfully")
            response = {
                "message": "Account created successfully",
                "data": serializer.data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


class LoginView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        """
            description - login a user
        """
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(email=email , password=password)

        if user:
            login(request, user)
            tokens = generate_auth_token(user)

            response = {
                "message": "login successfully",
                "tokens": tokens,
            }            
            return Response(data=response, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Invalid credentials"})
