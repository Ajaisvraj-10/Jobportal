from .views import *
from django.urls import path



urlpatterns = [
    path('',index,name='index'),
    path('login/',user_login,name='login'),
    path('register/',user_register,name='user_register'),
    path('logout/',user_logout,name='logout'),
    # path('company_register/',company_register,name='company_register'),
    path('create/',create,name='create'),
    



]