window.onload = function() {
    var pathArray = window.location.pathname;
    var lastElementIndex = pathArray.length - 1;
    $("#faq-a-" + pathArray[lastElementIndex]).addClass("a-active");
}

