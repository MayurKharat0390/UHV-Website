from django.urls import path
from . import views

app_name = 'reflections'

urlpatterns = [
    path('daily/', views.daily_reflection, name='daily_reflection'),
    path('submit/<int:scenario_id>/', views.submit_reflection, name='submit_reflection'),
]
