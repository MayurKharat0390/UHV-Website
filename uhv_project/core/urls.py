from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('uhv-cell/', views.uhv_cell, name='uhv_cell'),
    path('contact-us/', views.contact, name='contact'),
]
