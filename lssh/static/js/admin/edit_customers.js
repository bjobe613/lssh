





$('#change_payment_check').change(function() {
    if(document.getElementById('change_payment_check').checked) {
        $("#change_payment_div").removeClass('d-none')
    } else {
        $("#change_payment_div").addClass('d-none')
    } 
});


