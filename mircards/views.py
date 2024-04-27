from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import JsonResponse
from mircards import models
import pandas as pd

def search_mirna(request):
    if request.method == 'POST':
        user_input = request.POST.get('text1')
        try:
            query_res = models.Mircards.objects.using('local').get(Mature_id=user_input)
            return render(request, 'mircards/search_results.html', {'result': query_res})
        except models.Mircards.DoesNotExist:
            return render(request, 'mircards/search_results.html', {'error_message': 'No Mircards matching query'})
    else:
        return render(request, 'mircards/search_results.html')




# Create your views here.
def index(request):
    test = "test!!!!!!"
    return render(request,"mircards/index.html", {"a": test})

def handle(request):
    if request.method == 'POST':
        text = request.POST["搜索内容"]
        try:
            db = models.Sheet1.objects.using('search').get(mature_id=text)
            po_list = []
            po_list.append(db.mature_id)
            po_list.append(db.mature_seq)
            po_list.append(db.mature_seed_seq)
            po_list.append(db.mature_seed_same)
            po_list.append(db.mature_chrom)
            po_list.append(db.mature_pre_mir)
            po_list.append(db.mature_conf)
            po_list.append(db.mature_pre_name)
    # po_list['mature_seq'] = db.mature_seq
    # for i in db:
    #     if text in i.mature_id:
    #         po_list.append(i.mature_id)
            return render(request,"mircards/handle.html",{"resp":po_list})
        except models.Sheet1.DoesNotExist:
            return render(request, 'mircards/handle.html', {'error_message': 'No Sheet1 matching query'})



def checkSearch(request):
    text = request.POST.get("搜索内容")
    print(text)
    da = models.Sheet1.objects.using('search').filter(mature_id=text)
    if da:
        return HttpResponse("sousuozhengque")
    else:
        return HttpResponse("sousuocuowu")

def data(request):
    list = models.Sheet1.objects.all()
    return render(request,"mircards/data.html",{'res': list})


from .models import Sheet1
def download_excel(request):
    # 查询你的模型获取所有数据
    data_queryset = Sheet1.objects.all().values()
    df = pd.DataFrame(list(data_queryset))  # 转换查询集到DataFrame

    # 使用 pandas 的 ExcelWriter 创建一个Excel文件
    excel_path = 'my_data.xlsx'  # 文件存放路径和名称
    with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
        df.to_excel(writer, index=False)  # 写入数据到Excel，不包含行索引

    # 以二进制形式读取生成的Excel文件
    with open(excel_path, 'rb') as excel_file:
        response = HttpResponse(excel_file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    # 设置HTTP响应头部，使浏览器识别为文件下载
    response['Content-Disposition'] = f'attachment; filename="{excel_path}"'

    return response


