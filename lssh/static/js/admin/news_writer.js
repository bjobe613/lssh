var documentHasCanged = true;

function callOnDocumentChange() {
    documentHasCanged = true;
    $('#close-button').addClass('btn-warning')
    $('#close-button').removeClass('btn-secondary')
    $('#close-button').html('Close without saving')


}

function saveDocument() {
    documentHasCanged = false;
    $('#close-button').addClass('btn-secondary')
    $('#close-button').removeClass('btn-warning')
    $('#close-button').html('Close')

}
$(document).ready(function () {
    $('#news-header').change(callOnDocumentChange);
    $('#news-ingress').change(callOnDocumentChange);
    $('#save-button').click(function (e) {
        e.preventDefault();
        saveDocument();

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
    var editor = new Quill('#editor', quillOptions);

    //Adding event listeners to editor
    editor.on('text-change', function (delta, oldDelta, source) {
        callOnDocumentChange();
    });
})