var quillOptions = {
    modules: {
        toolbar: [
            [{header: [1, 2, false]}],
            ['bold', 'italic', 'underline'],
            ['image', 'link']

        ]
    },
    placeholder: 'Write the news article here...',
    theme: 'snow'
};
var editor = new Quill('#editor', quillOptions);