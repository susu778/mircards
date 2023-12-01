from django.shortcuts import render, HttpResponse
from .models import AdGene
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import mysite.settings as settings
import pickle
import pandas as pd
from .models import AdArticle


# Create your views here.
def index(request):
    query_set = AdGene.objects.using('local').all()
    return render(request, 'kgad/index.html', {"data": query_set})


def index_cn(request):
    query_set = AdGene.objects.using('local').all()
    return render(request, 'kgad/index_cn.html', {"data": query_set})


@csrf_exempt
def upload(request):
    if request.method == "POST":
        obj = request.FILES.get('exp')
        data_dir = str(settings.BASE_DIR)+"/kgad/static/kgad/data/"
        with open(data_dir + obj.name, "wb+") as destination:
            for chunk in obj.chunks():
                destination.write(chunk)
        mydata_dir = data_dir + obj.name
        mydata = pd.read_csv(mydata_dir,sep="\t",index_col=0)
        model_dir = data_dir + "svm.model"
        f = open(model_dir,'rb')
        s = f.read()
        model = pickle.loads(s)
        res_prob = model.predict_proba(mydata)
        result = []
        tmp = {}
        for i in range(len(res_prob)):
            if(res_prob[i][0] > res_prob[i][1]):
                tmp['sample'] = mydata.index[i]
                tmp['label'] = "Normal"
                prob1 = round(res_prob[i][0] * 100, 2)
                prob2 = "%.2f%%" % (prob1)
                tmp['prob'] = str(prob2)
                tmp['style'] = "green"
                result.append(tmp)
                tmp = {}
            else:
                tmp['sample'] = mydata.index[i]
                tmp['label'] = 'AD'
                prob1 = round(res_prob[i][1] * 100, 2)
                prob2 = "%.2f%%" % (prob1)
                tmp['prob'] = str(prob2)
                tmp['style'] = "red"
                result.append(tmp)
                tmp = {}
        return JsonResponse(result, safe=False)


@csrf_exempt
def article(request):
    if request.method == "POST":
        result = []
        tmp = {}
        article_no = request.POST.get('article_no')
        print(article_no)
        query_article = AdArticle.objects.using('local').filter(article_no=article_no)
        tmp['title'] = query_article[0].title
        tmp['content'] = query_article[0].content
        result.append(tmp)
    return JsonResponse(result,safe=False)

