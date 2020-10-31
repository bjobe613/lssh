
function clearForm() {
    $("#add-buyer-form").trigger("reset");
}


// Adds new buyer in the database
function addBuyer() {

    //checkbox value

    var internatonalBoolean;

    if ($("#checkbox-international:checked").val()) {
        internatonalBoolean = 1;
    } else {
        internatonalBoolean = 0;
    }


    data = {
        "liuid": $("#input-liuid-buyer").val(),
        "name": $("#input-name").val(),
        "email": $("#input-email").val(),
        "program": $("#input-program").val(),
        "international": internatonalBoolean
    }
    $.ajax({
        url: '/admin/buyingprocess/add_buyer',
        type: 'POST',
        contentType: "application/json",
        data: JSON.stringify(data),
        success: function (res) {

            
            $("#add-buyer-form").trigger("reset");
            $('#modal-add-buyer').modal('hide');
            location.reload();

        },
        error: function (error) {

        }
    });
}


// Adds new buyer in the database
function addSeller() {

    //checkbox value

    var internatonalBoolean;

    if ($("#checkbox-international:checked").val()) {
        internatonalBoolean = 1;
    } else {
        internatonalBoolean = 0;
    }


    data = {
        "liuid": $("#input-liuid-seller").val(),
        "name": $("#input-name-seller").val(),
        "email": $("#input-email-seller").val(),
        "program": $("#input-program-seller").val(),
        "international": internatonalBoolean,
        "phone": $("#input-phone-seller").val(),
        "payment": $("#input-payment-seller").val()
    }
    $.ajax({
        url: '/admin/buyingprocess/add_seller',
        type: 'POST',
        contentType: "application/json",
        data: JSON.stringify(data),
        success: function (res) {

            
            $("#add-seller-form").trigger("reset");
            $('#modal-add-seller').modal('hide');
            location.reload();

        },
        error: function (error) {

        }
    });
}


