from django.urls import path

from . import views

app_name = 'ams'
urlpatterns = [
    path('index', views.index),
    path('browse', views.browse),
    path('login', views.login),
    path('login1', views.login1),
    path('login2', views.login2),
    path('userlogin',views.userlogin),
]
