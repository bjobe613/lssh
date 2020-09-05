$("#edit-faq-question-form").submit(function (e) {
    e.preventDefault()
    var form = document.getElementById("edit-faq-question-form")
    var formData = new FormData(form);
    console.log(location.href.split('/')[6])
    $.ajax({
        url: '/faq/question/' + location.href.split('/')[6],
        type: 'PUT',
        data: formData,
        dataType: 'json',
        processData: false,
        contentType: false,
        success: function (response) {
            location.href = "/admin/faq/" + response.categoryID;
        },
        error: function (response) {
            alert("Something went wrong, couldn't edit faq. Error message: " + response.msg);
        }
    })
})