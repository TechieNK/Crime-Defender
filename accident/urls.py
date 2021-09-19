from django.urls import path
from accident import views

urlpatterns = [
    path('', views.home, name="home"),
    path('accident/',views.accident,name="accident"),
    path('results/',views.results,name="results")
]
