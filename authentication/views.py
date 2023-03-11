from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

# Create your views here.
class User(View):
    def get(self, request):
        return JsonResponse({'message': 'Testing'})