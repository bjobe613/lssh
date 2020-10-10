var productList = []

function addItem() {

    data = {
        "product_id": $("#input-product-id").val(),
    }



    $.ajax({
        url: '/admin/buyingprocess/data',
        type: 'POST',
        contentType: "application/json",
        data: JSON.stringify(data),
        success: function (res) {
            checkAndAddProduct(res)

        },
        error: function (error) {

        }

    });


}

function updateCart() {

    $("#content").html("");

    for (i = 0; i < productList.length; i++) {

        var html = '<div class="row product-row">'
            + '<div class="col-2">'
            + '<p>' + productList[i].articleNumber + '</p>'
            + '</div>'
            + '<div class="col-4">'
            + '<p>' + productList[i].name + '</p>'
            + '</div>'
            + '<div class="col-4">'
            + '<p> price </p>'
            + '</div>'
            + '</div>'

        $("#content").append(html);
    }
}

function checkAndAddProduct(res) {
    var product_duplicate = false;
    if (productList.length == 0) {
        productList.push(res)
        $("#input-product-id").val('')
        updateCart()
    } else {
        for (i = 0; i < productList.length; i++) {
            if (productList[i].articleNumber == res.articleNumber) {
                alert("Already added this product")
                $("#input-product-id").val('')
                product_duplicate = true;
            }
        }

        if (product_duplicate == false) {
            productList.push(res)
            $("#input-product-id").val('')
            updateCart()
        }

    }
}



/* Add this to give a warning when refreshing the page
window.onbeforeunload = function() {
    return "Data will be lost if you leave the page, are you sure?";
};*/