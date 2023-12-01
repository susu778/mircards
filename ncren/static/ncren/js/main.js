$(function(){
    //home页跳转
    $("#jump_browse").click(function(){
        $("#jump_b").click();
    });
    $("#jump_search").click(function(){
        $("#jump_s").click();
    });
    $("#jump_download").click(function(){
        $("#jump_d").click();
    });
    //查询框输入时查库,input下给提示
    $("#search_form").on("input", function () {
        $.ajax({
            type: 'get',
            url: '/ncrenapp/search_input/',
            data: {
                ncrna: $('#ncrna').val(),
                ef: $('#ef').val(),
                pheno: $('#pheno').val(),
                species: $('#species').val(),
            },
            success: function(data) {
                //console.log(data);
                ncrna_str = '';
                ef_str = '';
                pheno_str = '';
                species_str = '';
                if(data[0]['ncrna'] == 'true'){
                    for(var i=0; i<data[1].length; i++){
                        ncrna_str +="<option value=\""+ data[1][i]['ncrna']+"\">";
                    }
                    $("#rna_list").html(ncrna_str);
                }
                if(data[2]['ef'] == 'true'){
                    for(var i=0;i<data[3].length;i++){
                        ef_str += "<option value=\""+ data[3][i]['ef']+"\">";
                    }
                    $('#ef_list').html(ef_str);
                }
                if(data[4]['pheno'] == 'true'){
                    for(var i=0;i<data[5].length;i++){
                        pheno_str += "<option value=\""+ data[5][i]['phenotype']+"\">";
                    }
                    $('#pheno_list').html(pheno_str);
                }
                if(data[6]['species'] == 'true'){
                    for(var i=0;i<data[7].length;i++){
                        species_str += "<option value=\""+ data[7][i]['species']+"\">";
                    }
                    $('#species_list').html(species_str);
                }
            }
        });
    });
    //example, clear, btn
    $("#example_btn").click(function () {
        $("#ncrna").prop("value","hsa-mir-21");
        $("#ef").prop("value","H2O2");
    });
    $("#clear_btn").click(function () {
        $("#ncrna").prop("value","");
        $("#ef").prop("value","");
        $("#pheno").prop("value","");
        $("#species").prop("value","");
        $("#ncrna").focus();
    });
})