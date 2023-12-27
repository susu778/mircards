from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name="index"),
    path('home', views.home, name="home"),
    path('search', views.search, name="search"),
    path('mirset', views.mirset, name="mirset"),
    path('analysis', views.analysis, name="analysis"),
    path('download', views.download, name="download"),
    path('help', views.help, name="help"),
    path('about', views.about, name="about"),
]