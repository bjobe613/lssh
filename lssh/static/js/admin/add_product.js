$('document').ready(function(){
    document.getElementById("add-product-form").addEventListener('submit', function(e) {
        e.preventDefault();
        submitProductForm();
    });
})

/**
 * Used for submiting the form
 */
function submitProductForm() {
    var form = document.getElementById("add-product-form")
    var formData = new FormData(form);

    getFiles().forEach((file) => {
        formData.append('file', file);
    })
    
    $.ajax({
        url: '/products/add/',
        type: 'POST',
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


function searchValidSeller() {

    data = {
        "liuID": $("#valid-seller-input").val()
    }
    $.ajax({
        url: '/admin/check_valid_seller',
        type: 'POST',
        contentType: "application/json",
        data: JSON.stringify(data),
        success: function (res) {

     
            $("#add-product-sellerid").val(res);
            alert("Successful seller")
            

        },
        error: function (error) {

            alert("Invalid seller")

        }
    });
    

}
