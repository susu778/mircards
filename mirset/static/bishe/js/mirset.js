// 定义 Node 函数
var myChart = echarts.init(document.getElementById('graph'));
var searchResult = str1
//用表格列出所有的关系
tableData = []
for (var i = 0 ; i < searchResult.length ; i++){
    relationData = {} ;
    relationData['entity1'] = searchResult[i]['n1']['name'];
    relationData['relation'] = searchResult[i]['rel']['name'];
    relationData['entity2'] = searchResult[i]['n2']['name'] ;
    tableData.push(relationData) ;
}
jQuery(function(){
    $('.table').footable({
    "columns": [{"name":"entity1",title:"Entity1"} ,
              {"name":"relation",title:"Relation"},
              {"name":"entity2",title:"Entity2"}],
    "rows": tableData
    });
});

// 定义空数组用于存储节点数据
var data = [];
// 定义空数组用于存储关系数据
var links = [];

// 设定最大展示节点数
var maxDisplayNode = 10000;
// 初始化节点 ID
var id = 0;

// 循环遍历搜索结果，并构造展示的节点和关系数据
for (var i = 0; id < Math.min(maxDisplayNode, searchResult.length + 1) && i < searchResult.length; i++) {
    // 获取第一个节点（node1）
    var node1 = {};
    node1['name'] = searchResult[i]['n1']['name'];
    // 根据节点类型设置节点所属分类
    if (searchResult[i]['n1']['cate'] == ':MIRNA') {
        node1['category'] = 0;
    } else if (searchResult[i]['n1']['cate'] == ':KEY') {
        node1['category'] = 1;
    }

    var flag = 1;

    // 将节点1的ID转换为字符串，并初始化为relationTarget
    var relationTarget = id.toString();

    // 遍历已有节点数据，检查是否已存在相同节点
    for (var j = 0; j < data.length; j++) {
        if (data[j]['name'] === node1['name']) {
            flag = 0;
            relationTarget = data[j]['id'];
            break;
        }
    }

    // 将节点1的ID和节点1数据添加到data数组中
    node1['id'] = relationTarget;
    if (flag === 1) {
        id++;
        data.push(node1);
    }

    // 获取第二个节点（node2）
    var node2 = {};
    node2['name'] = searchResult[i]['n2']['name'];
    // 根据节点类型设置节点所属分类
    if (searchResult[i]['n2']['cate'] == ':MIRNA') {
        node2['category'] = 0;
    } else if (searchResult[i]['n2']['cate'] == ':KEY') {
        node2['category'] = 1;
    }

    flag = 1;
    relationTarget = id.toString();

    // 遍历已有节点数据，检查是否已存在相同节点
    for (var j = 0; j < data.length; j++) {
        if (data[j]['name'] === node2['name']) {
            flag = 0;
            relationTarget = data[j]['id'];
            break;
        }
    }

    // 将节点2的ID和节点2数据添加到data数组中
    node2['id'] = relationTarget;
    if (flag === 1) {
        id++;
        data.push(node2);
    }

    // 获取关系数据
    var relation = {};
    relation['source'] = node1['id'];
    relation['target'] = node2['id'];

    flag = 1;

    // 遍历已有关系数据，检查是否已存在相同关系
    for (var j = 0; j < links.length; j++) {
        if (links[j]['source'] == relation['source'] && links[j]['target'] == relation['target']) {
            links[j]['value'] = links[j]['value'] + searchResult[i]['rel']['name'];
            flag = 0;
            break;
        }
    }

    // 如果关系不存在，则添加关系数据到links数组中
    if (flag === 1) {
        relation['value'] = searchResult[i]['rel']['name'];
        relation['symbolSize'] = 10;
        links.push(relation);
    }
}


// Echarts初始化设置
option = {
    title: {
        text: 'neo4j'
    },

    toolbox: {
        // 显示工具箱
        show: true,
        feature: {
            mark: {
                show: true
            },
            // 还原
            restore: {
                show: true
            },
            // 保存为图片
            saveAsImage: {
                show: true
            }
        }
    },

    animationDurationUpdate: 1500,
    animationEasingUpdate: 'quinticInOut',
    label: {
        normal: {
            show: true,
            textStyle: {
                fontSize: 12
            },
        }
    },
    legend: {
        x: "center",
        show: false
    },
    series: [
        {
            type: 'graph',// 类型:关系图
            layout: 'force',//图的布局，类型为力导图
            symbolSize: 45,
            focusNodeAdjacency: true,
            roam: true,// 是否开启鼠标缩放和平移漫游。默认不开启。如果只想要开启缩放或者平移,可以设置成 'scale' 或者 'move'。设置成 true 为都开启
            edgeSymbol: ['none', 'arrow'],
            data: data,
            links: links,
            categories: [{
                name: ':MIRNA',
                itemStyle: {
                    normal: {
                        color: "#4592FF",
                    }
                }
            }, {
                name: ':KEY',
                itemStyle: {
                    normal: {
                        color: "#C71585",
                    }
                }
            }],
            label: {
                normal: {
                    show: true,
                    textStyle: {
                        fontSize: 12,
                    },
                }
            },
            force: {
                repulsion: 1000
            },
            edgeSymbolSize: [4, 50],
            edgeLabel: {
                normal: {
                    show: true,
                    textStyle: {
                        fontSize: 10
                    },
                    formatter: "{c}"
                }
            },
            lineStyle: {
                normal: {
                    opacity: 0.9,
                    width: 1.3,
                    curveness: 0,
                    color:"#262626",
                }
            }
        }
    ]
};

// 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);



