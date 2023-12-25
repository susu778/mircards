from django.urls import path
from . import views

app_name = 'ncren'
urlpatterns = [
    path("index", views.index),
    path("search", views.search),
    path("search_result", views.search_result),
    path("search_input", views.search_input),
    path("ztree", views.ztree),
    path("browse_node",views.browse_node),
]

