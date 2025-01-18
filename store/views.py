from django.shortcuts import render, redirect
from .models import Product, Category
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

def product(request,pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product': product})



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

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import SignUpForm

def register_user(request):
    form = SignUpForm(request.POST or None)  # Ensure we get POST data or an empty form

    if request.method == 'POST':
        if form.is_valid():
            user = form.save()  # Save the new user

            # Authenticate the user
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)  
                messages.success(request, "You have registered successfully.")
                return redirect('home')  # Redirect after successful registration
            else:
                messages.error(request, "Authentication failed. Please try again.")
                return redirect('register')

        else:
            # If the form is invalid, print errors for debugging
            print(form.errors)  # You can remove this in production
            messages.error(request, "There was an error in your registration. Please try again.")
            return render(request, 'register.html', {'form': form})

    # GET request will show the empty form
    return render(request, 'register.html', {'form': form})


def category(request, foo):
    foo = foo.replace('-', ' ') 
    try:
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', {'products': products, 'category': category})
    
    except Category.DoesNotExist:
        messages.error(request, "Oops, this category does not exist!")
        return redirect('home')


    
