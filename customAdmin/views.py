from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

def dashboard(request):
    return render(request, 'customAdmin/dashboard.html', {})
