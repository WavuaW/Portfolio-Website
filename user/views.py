from django.shortcuts import render
from user.models import User
from user.serializer import UserSerializer
from rest_framework.response import Response
from django.contrib import messages
from rest_framework.generics import GenericAPIView
from rest_framework import status



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
