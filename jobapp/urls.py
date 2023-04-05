from django.urls import path
from .views import *


urlpatterns = [
    path("", index, name="index"),
    path("profile/", profile, name="profile"),
    path("profile_details/<int:id>/", profile_details, name="profile_details"),
    path("create/", create, name="create"),
]
