from django.urls import path
from . import views

app_name = 'journals'

urlpatterns = [
    path('', views.journal_list, name='list'),
    path('create/', views.journal_create, name='create'),
    path('<int:pk>/', views.journal_detail, name='detail'),
]
