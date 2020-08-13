
//Scroll navbar
$(document).scroll(function () {
    var $nav = $("#navbar");
    $nav.toggleClass('scrolled', $(this).scrollTop() > 0);
});


if ( window.history.replaceState ) {
    window.history.replaceState( null, null, window.location.href );
}
