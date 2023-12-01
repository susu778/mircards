from django.urls import path

from . import views

app_name = 'kgad'
urlpatterns = [
    path('index', views.index, name='index'),
    path('index_cn', views.index_cn, name='index_cn'),
    path('upload', views.upload, name='upload'),
    path('article', views.article, name='article'),
]