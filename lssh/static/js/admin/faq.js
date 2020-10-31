function deleteQuestion(id) {
    if (window.confirm("Do you really want to delete that question?")) {
        $.ajax({
            url:'/faq/question/' + id,
            type: 'DELETE',
            dataType: 'json',
            success: function (response) {
                location.href = "/admin/faq/" + response.categoryID;
            },
            error: function (response) {
                alert("Something went wrong, couldn't delete faq. Error message: " + response.msg);
            }
        })
    }
}

function deleteCategory(id) {
    $.ajax({
        url:'/faq/category/' + id,
        type: 'DELETE',
        dataType: 'json',
        success: function (response) {
            location.href = "/admin/faq/";
        },
        error: function (response) {
            alert("Something went wrong, couldn't delete. Error message: " + response.msg);
        }
    })
}

$("#add-category-form").submit(function (e) {
    e.preventDefault();

    var form = document.getElementById("add-category-form")
    var formData = new FormData(form);

    $.ajax({
        url: '/faq/category/',
        type: 'POST',
        data: formData,
        dataType: 'json',
        processData: false,
        contentType: false,
        success: function (response) {
            location.href = "/admin/faq/" + response.id;
        },
        error: function (response) {
            alert("Something went wrong, couldn't add category. Error message: " + response.msg);
        }
    })
})

$("#edit-category-form").submit(function (e) {
    e.preventDefault();

    var form = document.getElementById("edit-category-form")
    var formData = new FormData(form);

    $.ajax({
        url: '/faq/category/' + location.href.split('/')[5],
        type: 'PUT',
        data: formData,
        dataType: 'json',
        processData: false,
        contentType: false,
        success: function (response) {
            location.href = "/admin/faq/" + response.id;
        },
        error: function (response) {
            alert("Something went wrong, couldn't add category. Error message: " + response.msg);
        }
    })
})