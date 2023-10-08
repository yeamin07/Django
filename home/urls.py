from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('login/',views.login, name='login'),
    path('signup/',views.signup, name='signup'),
    path('input/',views.StudentForm, name='StudentForm'),
    path('info/',views.getInfo,name='getInfo')
]