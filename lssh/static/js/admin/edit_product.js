$('document').ready(function(){
    document.getElementById("edit-product-form").addEventListener('submit', function(e) {
        e.preventDefault();
        submitProductForm();
    });
})

/**
 * Used for submiting the form
 */
function submitProductForm() {
    var form = document.getElementById("edit-product-form")
    console.log(form)
    var formData = new FormData(form);
/*
    fileList.forEach((file) => {
        formData.append('file', file);
    })
    */
    req_url = '/products/' + location.href.split("/")[6]
    console.log(req_url);
    
    $.ajax({
        url: req_url,
        type: 'PUT',
        data: formData,
        dataType: 'json',
        processData: false,
        contentType: false,
        success: function(response) {
            location.href = "/admin/products"
        },
        error: function(response) {
            console.log(response)
            alert("Something went wrong, message from server: " + response.responseJSON.msg);
        }
    })
}


function searchValidSeller(product_id) {

 

    data = {
        "liuID": $("#valid-seller-input").val(),
        "productID": product_id
    }
    $.ajax({
        url: '/admin/check_valid_seller',
        type: 'POST',
        contentType: "application/json",
        data: JSON.stringify(data),
        success: function (res) {

     
            $("#edit-product-seller").val(res);
            alert("Successful seller")
            

        },
        error: function (error) {

            alert("Invalid seller")

        }
    });
    



}
