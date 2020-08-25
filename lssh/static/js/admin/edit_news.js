function saveDocument() {
    documentHasCanged = false;
    $('#close-button').addClass('btn-secondary')
    $('#close-button').removeClass('btn-warning')
    $('#close-button').html('Close')

}

$( document ).ready(function () {
    //$('#news-header').val("TJABBA")
    $('#save-button').click(function (e) {
        e.preventDefault();
        saveDocument();
    })
})