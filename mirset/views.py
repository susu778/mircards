from django.shortcuts import render
from py2neo import Graph
import json
# Create your views here.

class neo4jconn:
    def __init__(self):
        self.graph = Graph("neo4j://localhost:7687", auth=("neo4j", "11111111"))  # 连接neo4j图数据库，加载neo4j.dump
    # 关系查询:如果有输入
    def findRelationByEntity1(self, entity1):
        result = self.graph.run("MATCH (n1{name:\"" + entity1 + "\"})- [rel] - (n2) RETURN n1,rel,n2").data()
        return result
    # 关系查询 如果为空，整个体系
    def all(self):
        answer = self.graph.run("MATCH (n1)- [rel] -> (n2) RETURN n1,rel,n2 LIMIT 150 ").data()
        return answer

def sortMirset(searchResult):#调整
    target_data = []
    for item in searchResult:
        n1 = {}
        n1['cate'] = str(item['n1'].labels)
        n1['name'] = item['n1']['name']
        rel = {}
        rel['name'] = item['rel'].__class__.__name__
        n2 = {}
        n2['cate'] = str(item['n2'].labels)
        n2['name'] = item['n2']['name']
        target_data.append({
            'n1': n1,
            'rel': rel,
            'n2': n2
        })
    return target_data



def index(request):
    if (request.GET):
        db = neo4jconn()
        entity1 = request.GET['entity1_text']
        # 若输入entity1,则输出与entity1有直接关系的实体和关系
        if (len(entity1) != 0 ):
            searchResult = db.findRelationByEntity1(entity1)
            newdata=sortMirset(searchResult)
            return render(request, 'mirset/index.html', {'searchResult': json.dumps(newdata, ensure_ascii=False)})
        # 为空 则输出部分图
        if (len(entity1) == 0 ):
            searchResult = db.all()
            newdata=sortMirset(searchResult)
            return render(request, 'mirset/index.html', {'searchResult': json.dumps(newdata, ensure_ascii=False)})

    return render(request, 'mirset/index.html',{})




