/**
 * A large improvement would be to encapsulate everything related to the picture selector in a separate class.
 */

// Used for storing files outside of the file list. Is updated each time the file selector is used.
var fileList = [];

$('document').ready(function(){
    document.getElementById("add-product-picture-viewer").innerHTML = document.getElementById("empty-files-card").innerHTML;

    const input = document.getElementById("add-product-picture-picker");

    input.addEventListener('change', function(){
        fileList = fileList.concat(Array.from(document.getElementById("add-product-picture-picker").files));
        document.getElementById("add-product-picture-picker").value = "";
        updateImageViewer();

    });

    document.getElementById("add-product-form").addEventListener('submit', function(e) {
        e.preventDefault();
        submitProductForm();
    });
})
/**
 * Updates the image viewer
 */
function updateImageViewer() {
    const viewer = document.getElementById("add-product-picture-viewer");

    if (fileList.length == 0) {
        viewer.innerHTML = document.getElementById("empty-files-card").innerHTML;
    } else {
        viewer.innerHTML = "";
        for(var i = 0; i<fileList.length; ++i) {
            viewer.innerHTML += generateImageCard(fileList[i], i);
        }
    }
}

/**
 * Generates a card for insertion in the DOM.
 * 
 * TODO: Escape HTML from variables for safety.
 * @param {file} file 
 * @param {number} index 
 */
function generateImageCard(file, index) {
    var cardHtml = `
    <div class="card add-product-card">
        <img class="card-img-top add-product-card-img" src="${URL.createObjectURL(file)}">
        <div class="card-body">
            <h5>${file.name}</h5>
        </div>
        <div class="card-footer add-product-card-footer">
            <button class="btn btn-light add-product-card-button" onClick="moveFileDown(${index}); updateImageViewer();" type="button"><i class="fa fa-arrow-left"></i></button>
            <button class="btn btn-light add-product-card-button" onClick="removeFile(${index}); updateImageViewer();" type="button"><i class="fa fa-times"></i></button>
            <button class="btn btn-light add-product-card-button" onClick="moveFileUp(${index}); updateImageViewer();" type="button"><i class="fa fa-arrow-right"></i></button>
        </div>
    </div>
    `;
    return cardHtml;
}

/**
 * Moves the specified element in fileList up
 * @param {Number} index 
 */
function moveFileUp(index) {
    if(index >= 0 && index < fileList.length-1) {
        var temp = fileList[index + 1];
        fileList[index+1] = fileList[index];
        fileList[index] = temp;
    }
}

/**
 * Moves the specified element in fileList down
 * @param {Number} index 
 */
function moveFileDown(index) {
    if(index > 0 && index < fileList.length) {
        var temp = fileList[index - 1];
        fileList[index - 1] = fileList[index];
        fileList[index] = temp;
    }
}

/**
 * Removes the specified element in fileList
 * @param {Number} index 
 */
function removeFile(index) {
    if(index >= 0 && index < fileList.length) {
        fileList.splice(index, 1)
    }
}

/**
 * Used for submiting the form
 */
function submitProductForm() {
    var form = document.getElementById("add-product-form")
    var data = new FormData(form);

    fileList.forEach((file) => {
        data.append('file', file);
    })

    for (var pair of data.entries()) {
        console.log(pair[0]+ ', ' + pair[1]); 
    }

    var request = new XMLHttpRequest();

    request.open("POST", "/products/add/");
    request.send(data);
}