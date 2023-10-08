from django.urls import path
from .views import *



urlpatterns = [
    path('fb_products/',product_list,name='product_list'),
    path('fb_products/<int:pk>/',product_detail,name='product_detail'),
]