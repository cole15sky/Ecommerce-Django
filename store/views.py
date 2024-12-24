from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms


def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


def about(request):
    return render(request, 'about.html', {})


def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')  # Use .get() here
        
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to a specific page after login
            else:
                return render(request, 'login.html', {'error': 'Invalid username or password'})
        else:
            return render(request, 'login.html', {'error': 'Both fields are required'})
    return render(request, 'login.html')



def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')

def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Authenticate the user using their credentials
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "You have registered successfully. Welcome!")
                return redirect('home')
            else:
                messages.error(request, "There was a problem logging you in. Please try again.")
        else:
            messages.error(request, "Oops, there was a problem. Try again.")
            return redirect('register')
    return render(request, 'register.html', {'form': form})
