// 定义 Node 函数
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

//echarts 数据
var data = [] ;
var links = [] ;

//构造展示的数据
var maxDisPlayNode = 100000 ;
var id = 0 ;
for( var i = 0 ;id < Math.min(maxDisPlayNode,searchResult.length+1) && i<searchResult.length ; i++ ){
    //获取node1
    node1 = {} ;
    node1['name'] = searchResult[i]['n1']['name'] ;
    node1['category'] = searchResult[i]['n1']['cate'];

    var flag = 1 ;

    relationTarget = id.toString() ;
    for(var j = 0 ; j<data.length ;j++){
        if(data[j]['name'] === node1['name']){
            flag = 0 ;
            relationTarget = data[j]['id'] ;
            break ;
        }
    }

    node1['id'] = relationTarget ;
    if(flag === 1){
        id++ ;
        data.push(node1) ;
    }

    //获取node2
    node2 = {} ;
    node2['name'] = searchResult[i]['n2']['name'] ;
    node2['category'] = searchResult[i]['n2']['cate'];

    flag = 1 ;
    relationTarget = id.toString() ;
    for(var j = 0 ; j<data.length ;j++){
        if(data[j]['name'] === node2['name']){
            flag = 0 ;
            relationTarget = data[j]['id'] ;
            break ;
        }
    }
    node2['id'] = relationTarget ;
    if(flag === 1){
        id++ ;
        data.push(node2) ;
    }

    //获取relation
    relation = {}
    relation['source'] = node1['id'];
    relation['target'] = node2['id'] ;

    flag = 1;
    for(var j = 0 ;j<links.length;j++){
        if(links[j]['source'] == relation['source'] && links[j]['target'] == relation['target']){
            links[j]['value'] = links[j]['value'] + searchResult[i]['rel']['name'] ;
            flag = 0 ;
            break ;
        }
    }
    if(flag === 1){
        relation['value'] = searchResult[i]['rel']['name'] ;
        relation['symbolSize'] = 10;
        links.push(relation) ;
    }

}
    // Echarts初始化设置
    var myChart = echarts.init(document.getElementById('graph'));

    option = {
        title: {
            text: ''
        },
        tooltip: {},
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
                type: 'graph',
                layout: 'force',
                symbolSize: 45,
                focusNodeAdjacency: true,
                roam: true,
                edgeSymbol: ['none', 'arrow'],
                categories: [{
                    name: 'MIRNA',
                    itemStyle: {
                        normal: {
                            color: "#4592FF",
                        }
                    }
                }, {
                    name: 'KEY',
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
                data: data,
                links: links,
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


    //knob
    $(function() {
        $(".knob").knob({
            'draw': function() {
                $(this.i).val(this.cv + '%')
            }
        })
    });

    //carousel
    $(document).ready(function() {

        $("#owl-slider").owlCarousel({
            navigation: true,
            slideSpeed: 300,
            paginationSpeed: 400,
            singleItem: true

        });
    });

    //custom select box

    $(function() {
        $('select.styled').customSelect();
    });

    /* ---------- Map ---------- */
    $(function() {
        $('#map').vectorMap({
            map: 'world_mill_en',
            series: {
                regions: [{
                    values: gdpData,
                    scale: ['#000', '#000'],
                    normalizeFunction: 'polynomial'
                }]
            },
            backgroundColor: '#eef3f7',
            onLabelShow: function(e, el, code) {
                el.html(el.html() + ' (GDP - ' + gdpData[code] + ')');
            }
        });
    });

    tagcloud({ //开启词云
        //参数名: 默认值
        selector: ".tagcloud", //元素选择器
        fontsize: 15, //基本字体大小
        radius: 55, //滚动半径
        mspeed: "slow", //滚动最大速度
        ispeed: "slow", //滚动初速度
        direction: 135, //初始滚动方向
        keep: true //鼠标移出组件后是否继续随鼠标滚动
    });

        $(function() {
        $('.tree li:has(ul)').addClass('parent_li').find(' > span').attr('title', 'Collapse this branch');
        $('.tree li.parent_li > span').on('click', function(e) {
            var children = $(this).parent('li.parent_li').find(' > ul > li');
            if (children.is(":visible")) {
                children.hide('fast');
                $(this).attr('title', 'Expand this branch').find(' > i').addClass('fa-plus-square').removeClass('fa-minus-square');
            } else {
                children.show('fast');
                $(this).attr('title', 'Collapse this branch').find(' > i').addClass('fa-minus-square').removeClass('fa-plus-square');
            }
            e.stopPropagation();
        });
    });