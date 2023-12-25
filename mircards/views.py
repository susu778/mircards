from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    test = "test!!!!!!"
    return render(request,"mircards/index.html", {"a": test})