
// "Global" variables to be used by function within buying process
var productList = [];
var sellerSortedList = [];
var buyer;


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

            /**********************************************************************************
            * Checks and adds to product array if there are not any duplicates of the product. 
            * If there are no duplicates executes updateCart to update html
            ***********************************************************************************/
            checkAndAddProduct(res);



        },
        error: function (error) {

        }
    });
}




function updateTotalPayment() {
    var totalSum = 0;
    for (i = 0; i < productList.length; i++) {
        totalSum = totalSum + productList[i].price * productList[i].boughtQuantity;
    }
    $("#total-payment").html('<p>' + totalSum + '</p>');
}

function updateTotalItems() {

    var totalItems = 0;

    for (i = 0; i < productList.length; i++) {
        totalItems = totalItems + productList[i].boughtQuantity;
    }


    $("#total-items").html('<p>' + totalItems + '</p>');
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

            buyer = res;
            addBuyerHtml(res);


        },
        error: function (error) {
        }
    });
}

function addBuyerHtml(res) {

    var buyerData = res;

    var htmlTableBuyer = '<div class="row align-items-center buyer-grey pt-3 pb-3">'
        + '<div class="col-lg-2 col-12">'
        + '<b><p class="mb-0">LIU ID</p></b>'
        + '<p class="mb-0">' + buyerData.liuID + '</p>'
        + '</div>'
        + '<div class="col-lg-2 col-12">'
        + '<b><p class="mb-0">Email</p></b>'
        + '<p class="mb-0">' + buyerData.email + '</p>'
        + '</div>'
        + '<div class="col-lg-2 col-12">'
        + '<b><p class="mb-0">Name</p></b>'
        + '<p class="mb-0">' + buyerData.name + '</p>'
        + '</div>'
        + '<div class="col-lg-2 col-12">'
        + '<b><p class="mb-0">Program</p></b>'
        + '<p class="mb-0">' + buyerData.program + '</p>'
        + '</div>'
        + '<div class="col-lg-2 col-12">'
        + '<b><p class="mb-0">International</p></b>'
        + '<p class="mb-0">' + buyerData.international + '</p>'
        + '</div>'
        + '<div class="col-lg-2 col-12">'
        + '<button id="remove-buyer-button" onClick="removeBuyer()" class="btn btn-danger">Remove</button>'
        + '</div>'
        + '</div>'



    $("#buyer-information").html(htmlTableBuyer);
    $("#input-liuid").val('');


}

function removeBuyer() {
    buyer = ""; // Is this a valid way to clear variables?
    $("#buyer-information").html('<p>No customer added</p>');
}





// updateCart should probably sort seller of LSSh or Seller
function updateCart() {

    // Updates html for total payment
    updateTotalPayment();

    // Updates html for total items
    updateTotalItems();

    $("#content").html("");

    for (k = 0; k < sellerSortedList.length; k++) {

        /* HTML for the table head row */
        var htmlTableHead = '<div class="row product-row-header align-items-center">'
            + '<div class="col-2">'
            + '<b><p class="mb-0">Picture</p></b>'
            + '</div>'
            + '<div class="col-2">'
            + '<b><p class="mb-0">Article number</p></b>'
            + '</div>'
            + '<div class="col-2">'
            + '<b><p class="mb-0">Name</p></b>'
            + '</div>'
            + '<div class="col-2">'
            + '<b><p class="mb-0">Price (SEK)</p></b>'
            + '</div>'
            + '<div class="col-3 text-center">'
            + '<b><p class="mb-0">Quantity</p></b>'
            + '</div>'
            + '</div>';

        if (sellerSortedList[k].sellerId == 1) {
            $("#content").append('<h2> LSSh </h2>');
            $("#content").append(htmlTableHead);
        } else {

            $("#content").append('<h3> Seller ID: #' + sellerSortedList[k].sellerId + '</h3>');
            $("#content").append(htmlTableHead);
        }

        var totalPrice = 0;




        for (i = 0; i < sellerSortedList[k].products.length; i++) {

            var htmlQuantity;

            if (sellerSortedList[k].products[i].quantity > 1) {
                htmlQuantity = '<button class="btn btn-secondary d-inline" id="' + sellerSortedList[k].products[i].articleNumber + '" onClick="decreaseQuantity(this.id)">-</button>'
                    + '<p class="mb-0 d-inline pl-4 pr-4">' + sellerSortedList[k].products[i].boughtQuantity + '</p>'
                    + '<button class="btn btn-secondary d-inline" id="' + sellerSortedList[k].products[i].articleNumber + '" onClick="increaseQuantity(this.id)">+</button>'


            } else {
                htmlQuantity = '<p class="mb-0 d-inline pl-4 pr-4">' + sellerSortedList[k].products[i].quantity + '</p>';
            }

            /* HTML for the regular table rows */
            var html = '<div class="row product-row align-items-center">'
                + '<div class="col-2">'
                + '<img class="img-fluid picture-height pb-1" src="../../pictures/' + sellerSortedList[k].products[i].picture + '"></img>' /* Is this really good?  */
                + '</div>'
                + '<div class="col-2">'
                + '<p class="mb-0">' + sellerSortedList[k].products[i].articleNumber + '</p>'
                + '</div>'
                + '<div class="col-2">'
                + '<p class="mb-0">' + sellerSortedList[k].products[i].name + '</p>'
                + '</div>'
                + '<div class="col-2">'
                + '<p class="mb-0">' + sellerSortedList[k].products[i].price + '</p>'
                + '</div>'


                + '<div class="col-3 text-center">' + htmlQuantity + '</div>'
                + '<div class="col-1">'
                + '<button class="btn btn-danger" id="' + sellerSortedList[k].products[i].articleNumber + '" onClick="removeProduct(this.id)">Remove</button><br>'
                + '</div>'

                + '</div>';

            totalPrice = totalPrice + sellerSortedList[k].products[i].price * sellerSortedList[k].products[i].boughtQuantity;

            $("#content").append(html);

        }


        $("#content").append('<p class="float-right">Total price: ' + totalPrice + '</p>');
        $("#content").append('<br><button class="float-right" id="' + sellerSortedList[k].sellerId + '" onClick="clickButton(this.id)">Payment done</button><br>');


    }



}

function increaseQuantity(productArticleNumber) {

    for (x = 0; x < productList.length; x++) {

        if (productList[x].articleNumber == productArticleNumber) {

            if (productList[x].boughtQuantity < productList[x].quantity) {
                productList[x].boughtQuantity = productList[x].boughtQuantity + 1;
                break;
            } else {
                alert("Can't add more items")
            }
        }
    }

    sortItemsBySeller();
    updateCart();
}

function decreaseQuantity(productArticleNumber) {

    for (x = 0; x < productList.length; x++) {

        if (productList[x].articleNumber == productArticleNumber) {

            if (productList[x].boughtQuantity > 1) {
                productList[x].boughtQuantity = productList[x].boughtQuantity - 1;
                break;
            } else {
                alert("Can't add more items")
            }
        }
    }

    sortItemsBySeller();
    updateCart();
}



function clickButton(buttonId) {
    removeSeller(buttonId);
}

function removeProduct(buttonArticleNumber) {
    removeProductListItem(buttonArticleNumber);
    sortItemsBySeller();
    updateCart();

}

function removeSeller(buttonId) {
    for (i = 0; i < sellerSortedList.length; i++) {

        if (sellerSortedList[i].sellerId == buttonId) {

            for (k = 0; k < sellerSortedList[i].products.length; k++) {
                console.log('removed article ' + sellerSortedList[i].products[k].articleNumber);

                // Removes each item from database

                data = {
                    "product_id": sellerSortedList[i].products[k].articleNumber,
                    "quantityToBuy": sellerSortedList[i].products[k].boughtQuantity,
                }

                $.ajax({
                    url: '/admin/buyingprocess/remove_product',
                    type: 'POST',
                    contentType: "application/json",
                    data: JSON.stringify(data),
                    success: function (res) {




                    },
                    error: function (error) {

                    }
                });





                removeProductListItem(sellerSortedList[i].products[k].articleNumber);
            }

            sellerSortedList.splice(i, 1);
            break;
        }

    }

    updateCart();

}


function removeProductListItem(artNr) {


    for (x = 0; x < productList.length; x++) {

        if (productList[x].articleNumber == artNr) {
            productList.splice(x, 1);
            break;
        }

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
        sortItemsBySeller();
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
            sortItemsBySeller();
            updateCart();
        }

    }
}










