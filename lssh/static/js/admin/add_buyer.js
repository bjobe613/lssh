
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

            alert("success!");
            $("#add-buyer-form").trigger("reset");
            $('#modal-add-buyer').modal('hide');

        },
        error: function (error) {

        }
    });
}