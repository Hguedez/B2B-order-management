from django.shortcuts import render
from django.contrib.auth import authenticate

def sign_in(request):
    return render(request, 'login.html')