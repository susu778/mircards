$("#file_sub").click(function(){
    var files = document.getElementById("exp").files;
    if(files.length === 0){
        alert("Please upload the file!")
    }
    else{
        var formdata = new FormData();
        formdata.append("exp",files[0]);
        $.ajax({
           url: "/kgad/upload",
           type: "post",
           data: formdata,
           contentType: false,
           processData: false,
           success: function(res){
               // console.log(res);
               $("#result_field").css("display", "block");
               var html_str = ""
               for(var i = 0;i<res.length;i++){
                   html_str += "<tr><td>"+res[i]['sample']+"</td><td style='color:"+res[i]['style']+"'>"+res[i]['label']+"</td>"+"<td>"+res[i]['prob']+"</td></tr>"
               }
               var dt = document.getElementById('res_content');
               dt.innerHTML = html_str;
           }
        });
    }
});

$("#article1").click(function (){
    var article_no = "article1"
    $.ajax({
       url: "/kgad/article",
       type: "post",
       data: {"article_no":article_no},
       success: function(res){
           console.log(res);
           var html_str = "<div style='text-align: center;margin-top:20px;'><h3>"+res[0]['title']+"</h3></div>"+res[0]['content']
           var dt = document.getElementById('article_content');
           dt.innerHTML = html_str;
       }
    });
});
$("#article2").click(function (){
    var article_no = "article2"
    $.ajax({
       url: "/kgad/article",
       type: "post",
       data: {"article_no":article_no},
       success: function(res){
           console.log(res);
           var html_str = "<div style='text-align: center;margin-top:20px;'><h3>"+res[0]['title']+"</h3></div>"+res[0]['content']
           var dt = document.getElementById('article_content');
           dt.innerHTML = html_str;
       }
    });
});
$("#article3").click(function (){
    var article_no = "article3"
    $.ajax({
       url: "/kgad/article",
       type: "post",
       data: {"article_no":article_no},
       success: function(res){
           console.log(res);
           var html_str = "<div style='text-align: center;margin-top:20px;'><h3>"+res[0]['title']+"</h3></div>"+res[0]['content']
           var dt = document.getElementById('article_content');
           dt.innerHTML = html_str;
       }
    });
});
$("#article4").click(function (){
    var article_no = "article4"
    $.ajax({
       url: "/kgad/article",
       type: "post",
       data: {"article_no":article_no},
       success: function(res){
           console.log(res);
           var html_str = "<div style='text-align: center;margin-top:20px;'><h3>"+res[0]['title']+"</h3></div>"+res[0]['content']
           var dt = document.getElementById('article_content');
           dt.innerHTML = html_str;
       }
    });
});
$("#article5").click(function (){
    var article_no = "article5"
    $.ajax({
       url: "/kgad/article",
       type: "post",
       data: {"article_no":article_no},
       success: function(res){
           console.log(res);
           var html_str = "<div style='text-align: center;margin-top:20px;'><h3>"+res[0]['title']+"</h3></div>"+res[0]['content']
           var dt = document.getElementById('article_content');
           dt.innerHTML = html_str;
       }
    });
});
$("#article6").click(function (){
    var article_no = "article6"
    $.ajax({
       url: "/kgad/article",
       type: "post",
       data: {"article_no":article_no},
       success: function(res){
           console.log(res);
           var html_str = "<div style='text-align: center;margin-top:20px;'><h3>"+res[0]['title']+"</h3></div>"+res[0]['content']
           var dt = document.getElementById('article_content');
           dt.innerHTML = html_str;
       }
    });
});
$("#article7").click(function (){
    var article_no = "article7"
    $.ajax({
       url: "/kgad/article",
       type: "post",
       data: {"article_no":article_no},
       success: function(res){
           console.log(res);
           var html_str = "<div style='text-align: center;margin-top:20px;'><h3>"+res[0]['title']+"</h3></div>"+res[0]['content']
           var dt = document.getElementById('article_content');
           dt.innerHTML = html_str;
       }
    });
});
$("#article8").click(function (){
    var article_no = "article8"
    $.ajax({
       url: "/kgad/article",
       type: "post",
       data: {"article_no":article_no},
       success: function(res){
           console.log(res);
           var html_str = "<div style='text-align: center;margin-top:20px;'><h3>"+res[0]['title']+"</h3></div>"+res[0]['content']
           var dt = document.getElementById('article_content');
           dt.innerHTML = html_str;
       }
    });
});
$("#article9").click(function (){
    var article_no = "article9"
    $.ajax({
       url: "/kgad/article",
       type: "post",
       data: {"article_no":article_no},
       success: function(res){
           console.log(res);
           var html_str = "<div style='text-align: center;margin-top:20px;'><h3>"+res[0]['title']+"</h3></div>"+res[0]['content']
           var dt = document.getElementById('article_content');
           dt.innerHTML = html_str;
       }
    });
});
$("#article10").click(function (){
    var article_no = "article10"
    $.ajax({
       url: "/kgad/article",
       type: "post",
       data: {"article_no":article_no},
       success: function(res){
           console.log(res);
           var html_str = "<div style='text-align: center;margin-top:20px;'><h3>"+res[0]['title']+"</h3></div>"+res[0]['content']
           var dt = document.getElementById('article_content');
           dt.innerHTML = html_str;
       }
    });
});
$("#article11").click(function (){
    var article_no = "article11"
    $.ajax({
       url: "/kgad/article",
       type: "post",
       data: {"article_no":article_no},
       success: function(res){
           console.log(res);
           var html_str = "<div style='text-align: center;margin-top:20px;'><h3>"+res[0]['title']+"</h3></div>"+res[0]['content']
           var dt = document.getElementById('article_content');
           dt.innerHTML = html_str;
       }
    });
});
$("#article12").click(function (){
    var article_no = "article12"
    $.ajax({
       url: "/kgad/article",
       type: "post",
       data: {"article_no":article_no},
       success: function(res){
           console.log(res);
           var html_str = "<div style='text-align: center;margin-top:20px;'><h3>"+res[0]['title']+"</h3></div>"+res[0]['content']
           var dt = document.getElementById('article_content');
           dt.innerHTML = html_str;
       }
    });
});
$("#article13").click(function (){
    var article_no = "article13"
    $.ajax({
       url: "/kgad/article",
       type: "post",
       data: {"article_no":article_no},
       success: function(res){
           console.log(res);
           var html_str = "<div style='text-align: center;margin-top:20px;'><h3>"+res[0]['title']+"</h3></div>"+res[0]['content']
           var dt = document.getElementById('article_content');
           dt.innerHTML = html_str;
       }
    });
});
$("#article14").click(function (){
    var article_no = "article14"
    $.ajax({
       url: "/kgad/article",
       type: "post",
       data: {"article_no":article_no},
       success: function(res){
           console.log(res);
           var html_str = "<div style='text-align: center;margin-top:20px;'><h3>"+res[0]['title']+"</h3></div>"+res[0]['content']
           var dt = document.getElementById('article_content');
           dt.innerHTML = html_str;
       }
    });
});
$("#article_cn1").click(function (){
    var article_no = "article_cn1"
    $.ajax({
       url: "/kgad/article",
       type: "post",
       data: {"article_no":article_no},
       success: function(res){
           console.log(res);
           var html_str = "<div style='text-align: center;margin-top:20px;'><h3>"+res[0]['title']+"</h3></div>"+res[0]['content']
           var dt = document.getElementById('article_content');
           dt.innerHTML = html_str;
       }
    });
});
$("#article_cn2").click(function (){
    var article_no = "article_cn2"
    $.ajax({
       url: "/kgad/article",
       type: "post",
       data: {"article_no":article_no},
       success: function(res){
           console.log(res);
           var html_str = "<div style='text-align: center;margin-top:20px;'><h3>"+res[0]['title']+"</h3></div>"+res[0]['content']
           var dt = document.getElementById('article_content');
           dt.innerHTML = html_str;
       }
    });
});
$("#article_cn3").click(function (){
    var article_no = "article_cn3"
    $.ajax({
       url: "/kgad/article",
       type: "post",
       data: {"article_no":article_no},
       success: function(res){
           console.log(res);
           var html_str = "<div style='text-align: center;margin-top:20px;'><h3>"+res[0]['title']+"</h3></div>"+res[0]['content']
           var dt = document.getElementById('article_content');
           dt.innerHTML = html_str;
       }
    });
});
$("#article_cn4").click(function (){
    var article_no = "article_cn4"
    $.ajax({
       url: "/kgad/article",
       type: "post",
       data: {"article_no":article_no},
       success: function(res){
           console.log(res);
           var html_str = "<div style='text-align: center;margin-top:20px;'><h3>"+res[0]['title']+"</h3></div>"+res[0]['content']
           var dt = document.getElementById('article_content');
           dt.innerHTML = html_str;
       }
    });
});
$("#article_cn5").click(function (){
    var article_no = "article_cn5"
    $.ajax({
       url: "/kgad/article",
       type: "post",
       data: {"article_no":article_no},
       success: function(res){
           console.log(res);
           var html_str = "<div style='text-align: center;margin-top:20px;'><h3>"+res[0]['title']+"</h3></div>"+res[0]['content']
           var dt = document.getElementById('article_content');
           dt.innerHTML = html_str;
       }
    });
});
$("#article_cn6").click(function (){
    var article_no = "article_cn6"
    $.ajax({
       url: "/kgad/article",
       type: "post",
       data: {"article_no":article_no},
       success: function(res){
           console.log(res);
           var html_str = "<div style='text-align: center;margin-top:20px;'><h3>"+res[0]['title']+"</h3></div>"+res[0]['content']
           var dt = document.getElementById('article_content');
           dt.innerHTML = html_str;
       }
    });
});
$("#article_cn7").click(function (){
    var article_no = "article_cn7"
    $.ajax({
       url: "/kgad/article",
       type: "post",
       data: {"article_no":article_no},
       success: function(res){
           console.log(res);
           var html_str = "<div style='text-align: center;margin-top:20px;'><h3>"+res[0]['title']+"</h3></div>"+res[0]['content']
           var dt = document.getElementById('article_content');
           dt.innerHTML = html_str;
       }
    });
});
$("#article_cn8").click(function (){
    var article_no = "article_cn8"
    $.ajax({
       url: "/kgad/article",
       type: "post",
       data: {"article_no":article_no},
       success: function(res){
           console.log(res);
           var html_str = "<div style='text-align: center;margin-top:20px;'><h3>"+res[0]['title']+"</h3></div>"+res[0]['content']
           var dt = document.getElementById('article_content');
           dt.innerHTML = html_str;
       }
    });
});
$("#article_cn9").click(function (){
    var article_no = "article_cn9"
    $.ajax({
       url: "/kgad/article",
       type: "post",
       data: {"article_no":article_no},
       success: function(res){
           console.log(res);
           var html_str = "<div style='text-align: center;margin-top:20px;'><h3>"+res[0]['title']+"</h3></div>"+res[0]['content']
           var dt = document.getElementById('article_content');
           dt.innerHTML = html_str;
       }
    });
});
$("#article_cn10").click(function (){
    var article_no = "article_cn10"
    $.ajax({
       url: "/kgad/article",
       type: "post",
       data: {"article_no":article_no},
       success: function(res){
           console.log(res);
           var html_str = "<div style='text-align: center;margin-top:20px;'><h3>"+res[0]['title']+"</h3></div>"+res[0]['content']
           var dt = document.getElementById('article_content');
           dt.innerHTML = html_str;
       }
    });
});
$("#article_cn11").click(function (){
    var article_no = "article_cn11"
    $.ajax({
       url: "/kgad/article",
       type: "post",
       data: {"article_no":article_no},
       success: function(res){
           console.log(res);
           var html_str = "<div style='text-align: center;margin-top:20px;'><h3>"+res[0]['title']+"</h3></div>"+res[0]['content']
           var dt = document.getElementById('article_content');
           dt.innerHTML = html_str;
       }
    });
});
$("#article_cn12").click(function (){
    var article_no = "article_cn12"
    $.ajax({
       url: "/kgad/article",
       type: "post",
       data: {"article_no":article_no},
       success: function(res){
           console.log(res);
           var html_str = "<div style='text-align: center;margin-top:20px;'><h3>"+res[0]['title']+"</h3></div>"+res[0]['content']
           var dt = document.getElementById('article_content');
           dt.innerHTML = html_str;
       }
    });
});
$("#article_cn13").click(function (){
    var article_no = "article_cn13"
    $.ajax({
       url: "/kgad/article",
       type: "post",
       data: {"article_no":article_no},
       success: function(res){
           console.log(res);
           var html_str = "<div style='text-align: center;margin-top:20px;'><h3>"+res[0]['title']+"</h3></div>"+res[0]['content']
           var dt = document.getElementById('article_content');
           dt.innerHTML = html_str;
       }
    });
});
$("#article_cn14").click(function (){
    var article_no = "article_cn14"
    $.ajax({
       url: "/kgad/article",
       type: "post",
       data: {"article_no":article_no},
       success: function(res){
           console.log(res);
           var html_str = "<div style='text-align: center;margin-top:20px;'><h3>"+res[0]['title']+"</h3></div>"+res[0]['content']
           var dt = document.getElementById('article_content');
           dt.innerHTML = html_str;
       }
    });
});