from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Mircards
def search_mirna(request):
    if request.method == 'POST':
        user_input = request.POST.get('text1')
        try:
            query_res = Mircards.objects.using('local').get(Mature_id=user_input)
            return render(request, 'mircards/search_results.html', {'result': query_res})
        except Mircards.DoesNotExist:
            return render(request, 'mircards/search_results.html', {'error_message': 'No Mircards matching query'})
    else:
        return render(request, 'mircards/search_results.html')
# Create your views here.
def index(request):
    test = "test!!!!!!"
    return render(request,"mircards/index.html", {"a": test})


