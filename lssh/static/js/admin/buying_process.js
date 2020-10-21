
function onPageReady() {

    // "Global" variables to be used by function within buying process
    var productList = [];
    var sellerSortedList = [];
    var seller;


    // Listeners

    document.getElementById("submit-item").addEventListener("click", function () {
        addItem();
    });

    document.getElementById("buyer-search").addEventListener("click", function () {
        searchExistingCustomer();
    });


    // Function that adds item if it exists in the data base
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
                checkAndAddProduct(res);
                updateTotalPayment();
                updateTotalItems();

            },
            error: function (error) {

            }
        });
    }


    function updateTotalPayment() {
        var totalSum = 0;
        for (i = 0; i < productList.length; i++) {
            totalSum = totalSum + productList[i].price;
        }
        $("#total-payment").html('<p>' + totalSum + '</p>');
    }

    function updateTotalItems() {
        $("#total-items").html('<p>' + productList.length + '</p>');
    }


    function searchExistingCustomer() {
        data = {
            "liu_id": $("#input-liuid").val(),
        }
        $.ajax({
            url: '/admin/buyingprocess/customer',
            type: 'POST',
            contentType: "application/json",
            data: JSON.stringify(data),
            success: function (res) {
                seller = res;
                $("#seller-information").html(seller.liuID);
                $("#input-liuid").val('');
            },
            error: function (error) {
            }
        });
    }


    // updateCart should probably sort seller of LSSh or Seller
    function updateCart() {


        sortItemsBySeller();

        /* OLD plot items
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
                + '</div>';

            $("#content").append(html);
        }*/

        $("#content").html("");


        for (k = 0; k < sellerSortedList.length; k++) {

            if (sellerSortedList[k].sellerId == 1) {
                $("#content").append('<h2> LSSh </h2>');
            } else {
                $("#content").append('<h2> Seller ID: #' + sellerSortedList[k].sellerId + '</h2>');
            }

            var totalPrice = 0;

            for (i = 0; i < sellerSortedList[k].products.length; i++) {


                var html = '<div class="row product-row">'
                    + '<div class="col-2">'
                   
                    + '<img class="img-fluid picture-height" src="../../pictures/' + sellerSortedList[k].products[i].picture + '"></img>' /* Is this really good? */ 
                    + '</div>'
                    + '<div class="col-2">'
                    + '<p>' + sellerSortedList[k].products[i].articleNumber + '</p>'
                    + '</div>'
                    + '<div class="col-2">'
                    + '<p>' + sellerSortedList[k].products[i].name + '</p>'
                    + '</div>'
                    + '<div class="col-4">'
                    + '<p>' + sellerSortedList[k].products[i].price + '</p>'
                    + '</div>'
                    + '</div>';

                totalPrice = totalPrice + sellerSortedList[k].products[i].price;

                $("#content").append(html);

            }


            $("#content").append('<p class="float-right">Total price: ' + totalPrice + '</p>');
            $("#content").append('<br><button id="button-buy-' + sellerSortedList[k].sellerId + '"class="float-right">Payment done</button><br>');


        }



    }

    function sortItemsBySeller() {

        var sellerIdsDuplicates = [];

        for (i = 0; i < productList.length; i++) {
            sellerIdsDuplicates.push(productList[i].seller);
        }

        // This line removes duplicate elements from the array sellerIdsDuplicates
        var sellerIdsUnique = [... new Set(sellerIdsDuplicates)];

        sellerSortedList.length = 0;

        for (i = 0; i < sellerIdsUnique.length; i++) {

            var sellerProductList = [];

            for (k = 0; k < productList.length; k++) {
                if (sellerIdsUnique[i] == productList[k].seller) {
                    sellerProductList.push(productList[k]);
                }
            }


            var sellerItems = {
                sellerId: sellerIdsUnique[i],
                products: sellerProductList
            };

            // Adds to global list sorted by sellers and each sellers items
            sellerSortedList.push(sellerItems);

        }

    }

    function checkAndAddProduct(res) {
        var product_duplicate = false;
        if (productList.length == 0) {
            productList.push(res);
            $("#input-product-id").val('');
            updateCart();
        } else {
            for (i = 0; i < productList.length; i++) {
                if (productList[i].articleNumber == res.articleNumber) {
                    alert("Already added this product");
                    $("#input-product-id").val('');
                    product_duplicate = true;
                }
            }

            if (product_duplicate == false) {
                productList.push(res);
                $("#input-product-id").val('');
                updateCart();
            }

        }
    }


}


$(document).ready(function () {
    onPageReady();
});



