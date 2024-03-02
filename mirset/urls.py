from django.urls import path
from mirset import views

urlpatterns = [
    path('index/', views.index, name='index'),
    # path()
]