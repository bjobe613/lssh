/* Used for storing files outside of the file list. Is updated each time the file selector is used. */
var fileList = [];

$('document').ready(function(){
    document.getElementById("add-product-picture-viewer").innerHTML = document.getElementById("empty-files-card").innerHTML;

    const input = document.getElementById("add-product-picture-picker");

    input.addEventListener('change', function(){
        fileList = fileList.concat(Array.from(document.getElementById("add-product-picture-picker").files));
        document.getElementById("add-product-picture-picker").value = "";
        updateImageViewer();

    });
})

function updateImageViewer() {
    const viewer = document.getElementById("add-product-picture-viewer");

    if (fileList.length == 0) {
        document.getElementById("add-product-picture-picker").innerHTML = document.getElementById("empty-files-card").innerHTML;
    } else {
        viewer.innerHTML = "";
        for(var i = 0; i<fileList.length; ++i) {
            viewer.innerHTML += generateImageCard(fileList[i], i);
        }
    }
}

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

function moveFileUp(index) {
    if(index >= 0 && index < fileList.length) {
        var temp = fileList[index + 1];
        fileList[index+1] = fileList[index];
        fileList[index] = temp;
    }
}

function moveFileDown(index) {
    if(index > 0 && index <= fileList.length) {
        var temp = fileList[index - 1];
        fileList[index - 1] = fileList[index];
        fileList[index] = temp;
    }
}

function removeFile(index) {
    if(index >= 0 && index <= fileList.length) {
        fileList.splice(index, index)
    }
}