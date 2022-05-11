from django.shortcuts import render, HttpResponse, redirect
from .forms import *
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.hashers import make_password

# Create your views here.
def perform_registeration(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(user.password)
            user.save()
            messages.success(request, 'Registration is Successfully!')
            return redirect('register')
        else:
            return render(request, 'account/registration.html', context={
                'form': form,
            })
    form = UserRegisterForm()
    return render(request, 'account/registration.html', context={
        'form': form,
    })

def perform_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return redirect("home")
            else:
                messages.error(request, 'Account is inactive!')
                return redirect('login')
        else:
            messages.error(request, 'User Credentials Invalid!')
            return redirect('login')

    form = UserLoginForm()
    return render(request, 'account/login.html', context={
        'form': form,
    })

def logoutUser(request):
    auth_logout(request)
    return redirect('login')