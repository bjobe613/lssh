


    //Scroll navbar
$(document).scroll(function () {
    var $nav = $("#navbar");
    $nav.toggleClass('scrolled', $(this).scrollTop() > 0);
});


if ( window.history.replaceState ) {
    window.history.replaceState( null, null, window.location.href );
}





if (window.location.href.indexOf("about") > -1) {
    $( "#navbar" ).removeClass( "fixed-top" );
} 


if (window.location.href.indexOf("help") > -1) {
    $( "#navbar" ).removeClass( "fixed-top" );
    
} 

if (window.location.href.indexOf("hand_in") > -1) {
    $( "#navbar" ).removeClass( "fixed-top" );
}

if (window.location.href.indexOf("products") > -1) {
    $( "#navbar" ).removeClass( "fixed-top" );
} 








