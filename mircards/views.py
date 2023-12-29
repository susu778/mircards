from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    test = "test!!!!!!"
    return render(request,"mircards/index.html",{"a": test})

def search(request):
    test = "test!!!!!!"
    return render(request,"mircards/search.html",{"a": test})
def mirset(request):
    test = "test!!!!!!"
    return render(request,"mircards/mirset.html",{"a": test})
def analysis(request):
    test = "test!!!!!!"
    return render(request,"mircards/analysis.html",{"a": test})
def download(request):
    test = "test!!!!!!"
    return render(request,"mircards/download.html",{"a": test})
def help(request):
    test = "test!!!!!!"
    return render(request,"mircards/help.html",{"a": test})
def about(request):
    test = "test!!!!!!"
    return render(request,"mircards/about.html",{"a": test})