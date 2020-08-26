var serverUrl = 'http://localhost:5000'

function hideForm() {

    data = {
        "email": $("#handin-email-input").val(),
        "items": $("#handin-number-items").val()
    }


    $.ajax({
        url: serverUrl + '/hand_in/hand_in_request',
        type: 'POST',
        contentType: "application/json",
        data: JSON.stringify(data),
        success: function (res) {

            $("#step1").hide();
            $("#handin-step-1").removeClass("selected-step");
            $("#handin-step-1").addClass("not-selected-step");

            $("#handin-step-2").removeClass("not-selected-step");
            $("#handin-step-2").addClass("selected-step");

            typeId = 'handin-type';
            conditionId = 'handin-condition';
            sellOrDonateId = 'handin-sell-or-donate';
            additonalInformationId = 'handin-additional-information';


            $("#step2").append('<h3>Information about items/s</h3>');

            for (i = 0; i < data.items; i++) {

                step2 = '<form class="mb-5">'
                    + '<div class="form-group">'
                    + '<label for="exampleFormControlInput1">Type of item</label>'
                    + '<input type="text" class="form-control" placeholder="Write type here... (E.g. Sofa)" id=' + typeId + (i + 1) + '>'
                    + '</div>'
                    + '<div class="form-group">'
                    + '<label for="exampleFormControlSelect1">Condition of item</label>'
                    + '<select class="form-control" id=' + conditionId + (i + 1) + '>'
                    + '<option>Very good</option>'
                    + '<option>Good</option>'
                    + '<option>Fair</option>'
                    + '</select>'
                    + '</div>'
                    + '<div class="form-group">'
                    + '<label for="exampleFormControlSelect1">Do you want to sell or donate the item?</label>'
                    + '<select class="form-control" id=' + sellOrDonateId + (i + 1) + '>'
                    + '<option>Sell item</option>'
                    + '<option>Donate</option>'
                    + '</select>'
                    + '</div>'
                    + '<div class="form-group">'
                    + '<label for="exampleFormControlInput1">Additional information (Optional)</label>'
                    + '<input type="text" class="form-control" id=' + additonalInformationId + (i + 1) + ' placeholder="Write information here... (E.g. Scratches">'
                    + '</div>'
                    + '</form>'

                $("#step2").append('<h5>Item ' + (i + 1) + '</h5>');
                $("#step2").append(step2);
            }

            $("#step2").append('<button type="submit" onclick="checkHandIn()" class="btn btn-primary btn-green mb-5">Submit</button>');


        },
        error: function (error) {
            alert("Någonting fel");
        }

    });

}


// This function checks if the hand in form is correctly filled in every field required. If true then submit if false, error message
function checkHandIn() {

    data = {
        "email": $("#handin-email-input").val(),
        "items": $("#handin-number-items").val()
    }

    typeId = '#handin-type';
    conditionId = '#handin-condition';
    sellOrDonateId = '#handin-sell-or-donate';
    additonalInformationId = '#handin-additional-information';

    var items = [];

    for (i = 0; i < data.items; i++) {

        item = {
            "type": $(typeId + (i + 1)).val(),
            "condition": $(conditionId + (i + 1)).val(),
            "sell_or_donate": $(sellOrDonateId + (i + 1)).val(),
            "additional_information": $(additonalInformationId + (i + 1)).val()
        }
        items[items.length] = item;

    }

    var errorCounter = 0;
    for (k = 0; k < data.items; k++) {
        if (items[k].type == "") {
            errorCounter++;
            $("#handin-type" + (k + 1)).addClass("is-invalid");
        }
    }

    if (errorCounter == 0) {
        submitHandIn();
    } else {
        $("#step2").append("Något fel. Fixa");
    }

}

function submitHandIn() {

    data = {
        "email": $("#handin-email-input").val(),
        "items": $("#handin-number-items").val()
    }

    typeId = '#handin-type';
    conditionId = '#handin-condition';
    sellOrDonateId = '#handin-sell-or-donate';
    additonalInformationId = '#handin-additional-information';

    var items = [];

    for (i = 0; i < data.items; i++) {

        item = {
            "type": $(typeId + (i + 1)).val(),
            "condition": $(conditionId + (i + 1)).val(),
            "sell_or_donate": $(sellOrDonateId + (i + 1)).val(),
            "additional_information": $(additonalInformationId + (i + 1)).val()
        }

        // Array which saves all item objects
        items[items.length] = item;

    }


    /* Hide previous step and change progress bar */
    $("#step2").hide();
    $("#handin-step-2").removeClass("selected-step");
    $("#handin-step-2").addClass("not-selected-step");

    $("#handin-step-3").removeClass("not-selected-step");
    $("#handin-step-3").addClass("selected-step");


    var utc = new Date().toJSON().slice(0, 10).replace(/-/g, '/');

    $("#step3").append('<h3>Confirmed!</h3>');
    $("#step3").append('<h5>We will be in contact with you shortly.</h5>');
    $("#step3").append('<p>Date: ' + utc + '</p>');



    for (k = 0; k < data.items; k++) {

        $("#step3").append('<h5>Item ' + (k + 1) + '</h5>');

        confirmationList = '<ul>'
            + '<li>Type: ' + items[k].type + '</li>'
            + '<li>Condition: ' + items[k].condition + '</li>'
            + '<li>Sell or Donate: ' + items[k].sell_or_donate + '</li>'
            + '<li>Additional information: ' + items[k].additional_information + '</li>'
        $("#step3").append(confirmationList);

    }

}