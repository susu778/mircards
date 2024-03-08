  function clearDefault(el) {
    if (el.defaultValue==el.value) el.value = ""
}

 function reset_item() {
             document.getElementById("Form").reset();
        }

function select(){
     var t=document.getElementById('mirna') ;
     t.style.display = 'none';
     var p=document.getElementById('pre') ;
     p.style.display="table-row";

}