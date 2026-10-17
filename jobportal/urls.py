from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('apply/', views.job_apply, name='job_apply'),
]