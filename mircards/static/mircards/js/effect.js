 function clearDefault(el) {
    if (el.defaultValue==el.value) el.value = ""
}
function example() {
            $.ajax({
                url: `/mircards/static/examples/hsa_mirnas.txt`,
                dataType: "text",
                success: function(text) {
                    document.getElementById('input').value = text;


                }
            })
        }


 function reset_item() {
             document.getElementById("Form").reset();
        }


