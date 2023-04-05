from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import *


# Create your views here.
def index(request):
    jobs = Mainuser.objects.all()
    gender = request.GET.get("gender")
    if gender:
        jobs = jobs.filter(gender=gender)
    context = {"jobs": jobs, "choices": Mainuser.gender_choices}

    return render(request, "index.html", context)


def create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        domain = request.POST.get("domain")
        about = request.POST.get("about")
        email = request.POST.get("email")
        profile = request.FILES.get("profile")
        uploadcv = request.FILES.get("cv_upload")
        Profile.objects.create(
            name=name,
            domain=domain,
            about=about,
            email=email,
            profile=profile,
            cv_upload=uploadcv,
        )
        return redirect("index")
    return render(request, "create.html")


def profile(request):
    return render(request, "profile.html")


def profile_details(request, id):
    content = Mainuser.objects.get(id=id)
    profile = Profile.objects.filter(article=content)
    context = {"jobs": content, "profile": profile}

    return render(request, "profile_details.html", content)
