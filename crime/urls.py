from django.urls import path
from crime import views

urlpatterns = [
    path('', views.home, name="home"),
]
