from django.urls import path
from . import views

app_name = 'voices'

urlpatterns = [
    path('', views.voice_list, name='list'),
]
