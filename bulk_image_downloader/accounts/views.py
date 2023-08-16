from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User
from .models import custom_user
from django.contrib.auth.decorators import login_required


def register(request):
    if request.user.is_authenticated:
        messages.error(request, 'User already logged in')
        print('User already logged in')
        return redirect('/')
    else:
        return render(request, 'register.html')


def register_new_user(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            print('User already logged in')
            return redirect('/')
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['password2']
        if password1 != password2:
            print('Password not matching')
            messages.error(request, 'Password not matching')
        elif custom_user.objects.filter(username=username).exists():
            print('Username already taken')
            messages.error(request, 'Username already taken')
        elif custom_user.objects.filter(email=email).exists():
            print('Email already taken')
            messages.error(request, 'Email already taken')
        else:
            user = custom_user.objects.create_user(
                username=username, email=email, password=password1)
            user.save()
            messages.success(request, 'User created successfully')
            return redirect('/accounts/login')
        return render(request, 'register.html')
    else:
        return render(request, 'register.html')


def user_login(request):
    if request.user.is_authenticated:
        print("User already logged in")
        return redirect('/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if custom_user.objects.filter(username=username).exists():
            user = authenticate(username=username, password=password)
            list = custom_user.objects.all()
            for x in list:
                print(x.username)
            if user is not None:
                login(request, user)
                print("User logged in")
                return redirect('/')
            else:
                print("Invalid credentials")
                messages.error(request, 'Invalid credentials')
                return redirect('/accounts/login')
        else:
            print("User doesn't exist")
            messages.error(request, "User doesn't exist")
            return redirect('/accounts/login')
    else:
        if request.user.is_authenticated:
            print("User already logged in")
            return redirect('/')
        else:
            return render(request, 'login.html')


@login_required(login_url='http://127.0.0.1:8000/accounts/login')
def user_logout(request):
    print("logging out")
    logout(request)
    return redirect('/')


def current_user(request):
    return render(request, 'user_profile.html')
