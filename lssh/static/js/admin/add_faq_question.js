$("#add-question-form").submit(function (e) {
    e.preventDefault()
    var form = document.getElementById("add-question-form")
    var formData = new FormData(form);

    $.ajax({
        url: '/faq/question/',
        type: 'POST',
        data: formData,
        dataType: 'json',
        processData: false,
        contentType: false,
        success: function (response) {
            location.href = "/admin/faq/" + response.categoryID;
        },
        error: function (response) {
            alert("Something went wrong, couldn't add faq. Error message: " + response.msg);
        }
    })
})