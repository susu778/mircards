# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
# import codecs
from .models import Ncren
# from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt,csrf_protect
# from xlwt import *
import os, glob, re, datetime, time
from django.core.paginator import Paginator, PageNotAnInteger, InvalidPage


def index(request):
    # ncrna_list = Ncren.objects.using('ncren').values('ncrna').distinct()
    return render('ncren/index.html', {})


# def check_file():
#     for fn in glob.glob("d:/cuilab/mysite/static/ncren/download/*.*"):
#         filectime = os.path.getctime(fn)
#         currenttime = time.time()
#         difftime = int(currenttime) - int(filectime)
#         if (difftime > 36000):  # 超过10小时的文件就删除掉,36000
#             os.remove(fn)


@csrf_exempt
def search_input(request):
    if request.method == 'GET':
        ncrna = request.GET.get('ncrna')
        ef = request.GET.get('ef')
        pheno = request.GET.get('pheno')
        species = request.GET.get('species')
        res_list = []
        if(ncrna):
            dic = {}
            dic['ncrna'] = 'true'
            res_list.append(dic)
            ncrna_res = Ncren.objects.using('ncren').filter(ncrna__icontains = ncrna).values('ncrna').distinct()[:10]
            res_list.append(list(ncrna_res))
        else:
            dic = {}
            dic['ncrna'] = 'none'
            res_list.append(dic)
            res_list.append(dic)
        if(ef):
            dic = {}
            dic['ef'] = 'true'
            res_list.append(dic)
            ef_res = Ncren.objects.using('ncren').filter(ef__icontains=ef).values('ef').distinct()[:10]
            res_list.append(list(ef_res))
        else:
            dic = {}
            dic['ef'] = 'none'
            res_list.append(dic)
            res_list.append(dic)
        if(pheno):
            dic = {}
            dic['pheno'] = 'true'
            res_list.append(dic)
            pheno_res = Ncren.objects.using('ncren').filter(phenotype__icontains=pheno).values('phenotype').distinct()[:10]
            res_list.append(list(pheno_res))
        else:
            dic = {}
            dic['pheno'] = 'none'
            res_list.append(dic)
            res_list.append(dic)
        if(species):
            dic = {}
            dic['species'] = 'true'
            res_list.append(dic)
            species_res = Ncren.objects.using('ncren').filter(species__icontains=species).values('species').distinct()[:10]
            res_list.append(list(species_res))
        else:
            dic = {}
            dic['species'] = 'none'
            res_list.append(dic)
            res_list.append(dic)
        return JsonResponse(res_list, safe=False)
    else:
        return None


@csrf_exempt
def search(request):
    if request.method == "GET":
        ncrna = request.GET['ncrna']
        ef = request.GET['ef']
        pheno = request.GET['pheno']
        species = request.GET['species']
        #后面再补充查询语句，假设先只查询ncrna
        res = Ncren.objects.using('ncren').filter(ncrna__icontains = ncrna, ef__icontains = ef, phenotype__icontains = pheno, species__icontains = species)
        paginator = Paginator(res, 15)
        page_res = paginator.page(1)
        page_num = paginator.num_pages
        if(page_num >= 10):
            page_range = range(1, 11)
        else:
            page_range = range(1, page_num)
        return render('ncren/search_result.html', {'ncrna':ncrna, 'ef': ef, 'pheno': pheno, 'species': species, 'page_res': page_res, 'page_range': page_range})


@csrf_exempt
def search_result(request):
    if request.is_ajax():
        page = request.GET.get('page')
        ncrna = request.GET.get('ncrna')
        ef = request.GET.get('ef')
        pheno = request.GET.get('pheno')
        species = request.GET.get('species')
        res = Ncren.objects.using('ncren').filter(ncrna__icontains=ncrna, ef__icontains = ef, phenotype__icontains = pheno, species__icontains = species)
        paginator = Paginator(res, 15)
        print(paginator.num_pages)
        page_num = int(page)
        if(page_num <= 6):
            if paginator.num_pages <= 10:
                page_range = range(1, paginator.num_pages+1)
                offset = page_num
            else:
                page_range =range(1,11)
                offset = page_num
        elif (page_num > 6) and (page_num <= paginator.num_pages - 5):
            page_range = range(page_num - 5, page_num + 5)
            offset = 6
        elif ( paginator.num_pages - 9 <= 0):
            page_range = range(1, paginator.num_pages + 1)
            offset = page_num
        else:
            page_range = range(paginator.num_pages - 9, paginator.num_pages + 1)
            offset = 10 - paginator.num_pages + page_num
        try:
            page_res = paginator.page(page)
        except PageNotAnInteger:
            page_res = paginator.page(1)
        except InvalidPage:
            page_res = paginator.page(paginator.num_pages)
        page_li = list(page_res.object_list.values())
        result = {'has_previous': page_res.has_previous(),
                  'has_next': page_res.has_next(),
                  'num_pages': page_res.paginator.num_pages,
                  'page_li': page_li,
                  'page_range': page_range,
                  'offset': offset}
        return JsonResponse(result)
    test = ''
    return HttpResponse(test)


@csrf_exempt
def ztree(request):
    if request.is_ajax():
        id = request.POST.get('id')
        name = request.POST.get('name')
        res = []
        # miRNA human
        if id == '100' and name == 'Human':
            mir_human = Ncren.objects.using('ncren').filter(ncrna_type='miRNA', species='Human').values_list('ncrna').distinct().order_by('ncrna')
            for i in range(len(mir_human)):
                dic = {}
                dic['pId'] = '100'
                dic['name'] = mir_human[i]
                res.append(dic)
            return JsonResponse(res, safe=False)
        # miRNA mouse
        if id == '101' and name == 'Mouse':
            mir_mouse = Ncren.objects.using('ncren').filter(ncrna_type='miRNA', species='Mouse').values_list('ncrna').distinct().order_by('ncrna')
            for i in range(len(mir_mouse)):
                dic = {}
                dic['pId'] = '101'
                dic['name'] = mir_mouse[i]
                res.append(dic)
            return JsonResponse(res, safe=False)
        # miRNA Rat
        if id == '102' and name == 'Rat':
            mir_rat = Ncren.objects.using('ncren').filter(ncrna_type='miRNA', species='Rat').values_list('ncrna').distinct().order_by('ncrna')
            for i in range(len(mir_rat)):
                dic = {}
                dic['pId'] = '102'
                dic['name'] = mir_rat[i]
                res.append(dic)
            return JsonResponse(res, safe=False)
        # miRNA Other
        if id == '103' and name == 'Other':
            mir_other = Ncren.objects.using('ncren').filter(ncrna_type='miRNA').exclude(species='Human').exclude(species='Mouse').exclude(species='Rat').values_list('ncrna').distinct().order_by('ncrna')
            for i in range(len(mir_other)):
                dic = {}
                dic['pId'] = '103'
                dic['name'] = mir_other[i]
                res.append(dic)
            return JsonResponse(res, safe=False)
        #lncRNA Human
        if id == '110' and name == 'Human':
            lnc_human = Ncren.objects.using('ncren').filter(ncrna_type='lncRNA', species='Human').values_list('ncrna').distinct().order_by('ncrna')
            for i in range(len(lnc_human)):
                dic = {}
                dic['pId'] = '110'
                dic['name'] = lnc_human[i]
                res.append(dic)
            return JsonResponse(res, safe=False)
        # lncRNA Mouse
        if id == '111' and name == 'Mouse':
            lnc_mouse = Ncren.objects.using('ncren').filter(ncrna_type='lncRNA', species='Mouse').values_list('ncrna').distinct().order_by('ncrna')
            for i in range(len(lnc_mouse)):
                dic = {}
                dic['pId'] = '111'
                dic['name'] = lnc_mouse[i]
                res.append(dic)
            return JsonResponse(res, safe=False)
        # lncRNA Rat
        if id == '112' and name == 'Rat':
            lnc_rat = Ncren.objects.using('ncren').filter(ncrna_type='lncRNA', species='Rat').values_list('ncrna').distinct().order_by('ncrna')
            for i in range(len(lnc_rat)):
                dic = {}
                dic['pId'] = '112'
                dic['name'] = lnc_rat[i]
                res.append(dic)
            return JsonResponse(res, safe=False)
        # lncRNA Other
        if id == '113' and name == 'Other':
            lnc_other = Ncren.objects.using('ncren').filter(ncrna_type='lncRNA').exclude(species='Human').exclude(species='Mouse').exclude(species='Rat').values_list('ncrna').distinct().order_by('ncrna')
            for i in range(len(lnc_other)):
                dic = {}
                dic['pId'] = '113'
                dic['name'] = lnc_other[i]
                res.append(dic)
            return JsonResponse(res, safe=False)
            # circRNA Human
        if id == '120' and name == 'Human':
            circ_human = Ncren.objects.using('ncren').filter(ncrna_type='circRNA', species='Human').values_list('ncrna').distinct().order_by('ncrna')
            for i in range(len(circ_human)):
                dic = {}
                dic['pId'] = '120'
                dic['name'] = circ_human[i]
                res.append(dic)
            return JsonResponse(res, safe=False)
        # circRNA Mouse
        if id == '121' and name == 'Mouse':
            circ_mouse = Ncren.objects.using('ncren').filter(ncrna_type='circRNA', species='Mouse').values_list('ncrna').distinct().order_by('ncrna')
            for i in range(len(circ_mouse)):
                dic = {}
                dic['pId'] = '121'
                dic['name'] = circ_mouse[i]
                res.append(dic)
            return JsonResponse(res, safe=False)
        # circRNA Rat
        if id == '122' and name == 'Rat':
            circ_rat = Ncren.objects.using('ncren').filter(ncrna_type='circRNA', species='Rat').values_list('ncrna').distinct().order_by('ncrna')
            for i in range(len(circ_rat)):
                dic = {}
                dic['pId'] = '122'
                dic['name'] = circ_rat[i]
                res.append(dic)
            return JsonResponse(res, safe=False)
        # circRNA Other
        if id == '123' and name == 'Other':
            circ_other = Ncren.objects.using('ncren').filter(ncrna_type='circRNA').exclude(species='Human').exclude(species='Mouse').exclude(species='Rat').values_list('ncrna').distinct().order_by('ncrna')
            for i in range(len(circ_other)):
                dic = {}
                dic['pId'] = '123'
                dic['name'] =circ_other[i]
                res.append(dic)
            return JsonResponse(res, safe=False)
        # Environmental factor
        if id == '2' and name == 'Environmental factor':
            ef = Ncren.objects.using('ncren').all().values_list('ef').distinct().order_by('ef')
            for i in range(len(ef)):
                dic = {}
                dic['pId'] = '2'
                dic['name'] = ef[i]
                res.append(dic)
            return JsonResponse(res, safe=False)
            # Environmental factor
        if id == '3' and name == 'Phenotype':
            pheno = Ncren.objects.using('ncren').all().values_list('phenotype').distinct().order_by('phenotype')
            for i in range(len(pheno)):
                dic = {}
                dic['pId'] = '3'
                dic['name'] = pheno[i]
                res.append(dic)
            return JsonResponse(res, safe=False)
    else:
        return False

@csrf_exempt
def browse_node(request):
    if request.is_ajax():
        node = request.GET.get('node')
        pid = request.GET.get('pid')
        node_res = []
        if pid != '2' and pid != '3':
            if pid == '100' or pid == '110' or pid == '120':
                node_query = Ncren.objects.using('ncren').filter(ncrna=node, species='Human')
                for i in node_query:
                    dic = {}
                    dic['ncrna'] = i.ncrna
                    dic['ef'] = i.ef
                    dic['pheno'] = i.phenotype
                    dic['ef_condition'] = i.ef_condition
                    dic['sample'] = i.sample
                    dic['evidence'] = i.evidence
                    dic['pmid'] = i.pmid
                    dic['species'] = i.species
                    node_res.append(dic)
                return JsonResponse(node_res, safe = False)
            elif pid == '101' or pid == '111' or pid == '121':
                node_query = Ncren.objects.using('ncren').filter(ncrna=node, species='Mouse')
                for i in node_query:
                    dic = {}
                    dic['ncrna'] = i.ncrna
                    dic['ef'] = i.ef
                    dic['pheno'] = i.phenotype
                    dic['ef_condition'] = i.ef_condition
                    dic['sample'] = i.sample
                    dic['evidence'] = i.evidence
                    dic['pmid'] = i.pmid
                    dic['species'] = i.species
                    node_res.append(dic)
                return JsonResponse(node_res, safe = False)
            elif pid == '102' or pid == '112' or pid == '122':
                node_query = Ncren.objects.using('ncren').filter(ncrna=node, species='Rat')
                for i in node_query:
                    dic = {}
                    dic['ncrna'] = i.ncrna
                    dic['ef'] = i.ef
                    dic['pheno'] = i.phenotype
                    dic['ef_condition'] = i.ef_condition
                    dic['sample'] = i.sample
                    dic['evidence'] = i.evidence
                    dic['pmid'] = i.pmid
                    dic['species'] = i.species
                    node_res.append(dic)
                return JsonResponse(node_res, safe = False)
            else:
                node_query = Ncren.objects.using('ncren').filter(ncrna=node).exclude(species='Human').exclude(species='Mouse').exclude(species='Rat')
                for i in node_query:
                    dic = {}
                    dic['ncrna'] = i.ncrna
                    dic['ef'] = i.ef
                    dic['pheno'] = i.phenotype
                    dic['ef_condition'] = i.ef_condition
                    dic['sample'] = i.sample
                    dic['evidence'] = i.evidence
                    dic['pmid'] = i.pmid
                    dic['species'] = i.species
                    node_res.append(dic)
                return JsonResponse(node_res, safe = False)
        if pid == '2':
            node_query = Ncren.objects.using('ncren').filter(ef=node).order_by('ncrna')
            for i in node_query:
                dic = {}
                dic['ncrna'] = i.ncrna
                dic['ef'] = i.ef
                dic['pheno'] = i.phenotype
                dic['ef_condition'] = i.ef_condition
                dic['sample'] = i.sample
                dic['evidence'] = i.evidence
                dic['pmid'] = i.pmid
                dic['species'] = i.species
                node_res.append(dic)
            return JsonResponse(node_res, safe = False)
        if pid == '3':
            node_query = Ncren.objects.using('ncren').filter(phenotype=node).order_by('ncrna')
            for i in node_query:
                dic = {}
                dic['ncrna'] = i.ncrna
                dic['ef'] = i.ef
                dic['pheno'] = i.phenotype
                dic['ef_condition'] = i.ef_condition
                dic['sample'] = i.sample
                dic['evidence'] = i.evidence
                dic['pmid'] = i.pmid
                dic['species'] = i.species
                node_res.append(dic)
            return JsonResponse(node_res, safe = False)