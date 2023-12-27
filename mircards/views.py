from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    test = "test!!!!!!"
    return render(request,"mircards/index.html", {"a": test})
def home(request):
    return render(request,"mircards/home.html")
def search(request):
    return render(request,"mircards/search.html")
def mirset(request):
    return render(request,"mircards/mirset.html")
def analysis(request):
    return render(request,"mircards/analysis.html")
def download(request):
    return render(request,"mircards/download.html")
def help(request):
    return render(request,"mircards/help.html")
def about(request):
    return render(request,"mircards/about.html")