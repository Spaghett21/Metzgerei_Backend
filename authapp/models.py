from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
import json


def register(request):
    if request.method == "Post":
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")
        if User.objects.filter(username=username).exists():
            return JsonResponse({"error": "Username already exsists"}, status = 400)
        user = User.objects.create_user(username=username, password=password)
        return JsonResponse({"message": "User created sucessfully"})
    

def user_login(request):
    if request.method == "Post":
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({"message": "Login sucessful"})
        return JsonResponse({"error": "Invalid credentials"}, status=400)    
    
def user_logout(request):
    logout(request)
    return JsonResponse({"message": "Logged out sucessfully"})
