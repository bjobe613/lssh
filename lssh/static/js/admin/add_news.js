$(document).ready(function () {
    $("#save-button").click(function () {
        var article = document.querySelector('input[name=article]');
        article.value = JSON.stringify(editor.getContents());

        var form = document.getElementById("add-news-form")
        var formData = new FormData(form);

        $.ajax({
            url: '/news/',
            type: 'POST',
            data: formData,
            dataType: 'json',
            processData: false,
            contentType: false,
            success: function (response) {
                location.href = "/admin/news/edit/" + response.id
            },
            error: function (response) {
                alert("Something went wrong, couldn't save document");
            }
        })
    })
})