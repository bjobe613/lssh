/**
 * A large improvement would be to encapsulate everything related to the picture selector in a separate class.
 */

// Used for storing files outside of the file list. Is updated each time the file selector is used.
let fileList = [];

let emptyCardHTML = `
<div class="card add-product-card">
    <img class="card-img-top add-product-card-img" src="/placeholder.png">
        <div class="card-body">
            <h5>No pictures chosen</h5>
        </div>
    <div class="card-footer add-product-card-footer">
        <button class="btn btn-light add-product-card-button" disabled><i class="fa fa-arrow-left"></i></button>
        <button class="btn btn-light add-product-card-button" disabled><i class="fa fa-times"></i></button>
        <button class="btn btn-light add-product-card-button" disabled><i class="fa fa-arrow-right"></i></button>
    </div>
</div>`

$('document').ready(function(){
    document.getElementById("picture-selector").innerHTML = `<div class="card-deck add-product-card-holder" id="picture-selector-inner">${emptyCardHTML}</div>`
    const input = document.getElementById("add-product-picture-picker");

    input.addEventListener('change', function(){
        fileList = fileList.concat(Array.from(document.getElementById("add-product-picture-picker").files));
        document.getElementById("add-product-picture-picker").value = "";
        updateImageViewer();
    });
})
/**
 * Updates the image viewer
 */
function updateImageViewer() {
    const viewer = document.getElementById("picture-selector-inner");

    if (fileList.length == 0) {
        viewer.innerHTML = emptyCardHTML;
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
 * Returns the filelist for usage outside
 */
function getFiles() {
    return fileList;
}
