from django.urls import path
from . import views

app_name = 'innovations'

urlpatterns = [
    path('', views.innovation_list, name='list'),
    path('<slug:slug>/', views.innovation_detail, name='detail'),
]
