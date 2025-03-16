from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('cart/', views.show_cart, name='cart'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
]
