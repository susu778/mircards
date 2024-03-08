from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name="index"),
    path('search_mirna', views.search_mirna),


]