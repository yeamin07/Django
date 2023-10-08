from django.urls import path
from moviebase import views

urlpatterns = [
    path('',views.home,name='home'),
    path('movie/<slug:key>',views.onemovie,name='oneMovie'),
    path('actor/<slug:key>',views.oneActor,name='oneActor'),
    path('director/<slug:key>',views.oneDirector,name='oneDirector'),
]