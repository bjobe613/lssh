function saveDocument() {
    var article = document.querySelector('input[name=article]');
    article.value = JSON.stringify(editor.getContents());

    var form = document.getElementById("add-news-form")
    var formData = new FormData(form);

    $.ajax({
        url: '/news/api/' + $("#id-holder").html(),
        type: 'PUT',
        data: formData,
        dataType: 'json',
        processData: false,
        contentType: false,
        success: function (response) {
            documentHasCanged = false;
            $('#close-button').addClass('btn-secondary')
            $('#close-button').removeClass('btn-warning')
            $('#close-button').html('Close')
        },
        error: function (response) {
            alert("Something went wrong, couldn't save document");
        }
    })

}

$(document).ready(function () {
    //$('#news-header').val("TJABBA")
    $('#save-button').click(function (e) {
        e.preventDefault();
        saveDocument();
    })

    $.ajax({
        url: '/news/api/' + $("#id-holder").html(),
        type: 'GET',
        dataType: 'json',
        success: function (response) {
            if (response.imgpath) {
                $("#picture-holder").html('<img class="img-fluid" src="/pictures/' + response.imgpath + '">')
            }
            $("#news-header").val(response.title)
            $("#news-ingress").val(response.ingress)
            editor.setContents(response.text)
        },
        error: function (response) {
            alert("Something went wrong, couldn't fetch data");
        }
    })

    saveDocument()
})