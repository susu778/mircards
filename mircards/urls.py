from django.urls import path
from . import views

app_name = 'mircards'

urlpatterns = [
    path('index', views.index),
    path('search_mirna', views.search_mirna),
    path('handle',views.handle,name='handle'),
    path('checkSearch/',views.checkSearch,name='checkSearch'),
    path('data/',views.data,name='data'),
    path('download_excel/',views.download_excel,name='download_excel')
]