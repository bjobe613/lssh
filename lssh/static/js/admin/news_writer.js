var editor;
var documentHasCanged = true;

function callOnDocumentChange() {
    documentHasCanged = true;
    $('#close-button').addClass('btn-warning')
    $('#close-button').removeClass('btn-secondary')
    $('#close-button').html('Close without saving')


}


$(document).ready(function () {
    $('#news-header').change(callOnDocumentChange);
    $('#news-ingress').change(callOnDocumentChange);

    const input = document.getElementById("add-product-picture-picker");

    $('#news-picture').change(function() {
        console.log("AAAA")
        file = document.getElementById('news-picture').files[0];
        $("#picture-holder").html('<img class="img-fluid" src="' + URL.createObjectURL(file) + '">')
    })

    //Creation of the editor
    var quillOptions = {
        modules: {
            toolbar: [
                [{ header: [1, 2, false] }],
                ['bold', 'italic', 'underline'],
                ['image', 'link']

            ]
        },
        placeholder: 'Write the news article here...',
        theme: 'snow'
    };
    editor = new Quill('#editor', quillOptions);

    //Adding event listeners to editor
    editor.on('text-change', function (delta, oldDelta, source) {
        callOnDocumentChange();
    });
})