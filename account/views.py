from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from jobapp.models import Mainuser, Profile

# Create your views here.


def user_register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        name = request.POST.get("name")
        gender = request.POST.get("gender")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        password1 = request.POST.get("password")
        password2 = request.POST.get("confirm_password")

        if password1 == password2:
            User.objects.create_user(
                username=username,
                first_name=name,
                password=password1,
                email=email,
                phone=phone,
                gender=gender,
            )
            return redirect("login", {"choices": Mainuser.gender_choices})
        else:
            messages.error(request, "Password Does Not Match")

    return render(request, "user_register.html")


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("index")

    return render(request, "account/login.html")


def user_logout(request):
    logout(request)
    return redirect("login")


def company_register(request):
    return render(request, "company_register.html")
