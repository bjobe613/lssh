
//Scroll navbar
$(document).scroll(function () {
    var $nav = $("#navbar");
    $nav.toggleClass('scrolled', $(this).scrollTop() > 0);
});

if (window.history.replaceState) {
    window.history.replaceState(null, null, window.location.href);
}

if (window.location.href.indexOf("about") > -1) {
    $( "#navbar" ).removeClass( "fixed-top" );
    $("#about-us-link").addClass("a-link-white-active");
  
} 


if (window.location.href.indexOf("find_us") > -1) {
    $("#find-link").addClass("a-link-white-active");
}

if (window.location.href.indexOf("transport") > -1) {
    $( "#navbar" ).removeClass( "fixed-top" );
}

if (window.location.href.indexOf("news") > -1) {
    $( "#navbar" ).removeClass( "fixed-top" );
} 



if (window.location.href.indexOf("admin_login") > -1) {
    $( "#navbar" ).addClass( "fixed-top" );
} 

if (window.location.href.indexOf("help") > -1) {
    $( "#navbar" ).removeClass( "fixed-top" );
} 

if (window.location.href.indexOf("hand_in") > -1) {
    $("#navbar").removeClass("fixed-top");
}

if (window.location.href.indexOf("products") > -1) {
    $("#navbar").removeClass("fixed-top");
}

if (window.location.href.indexOf("contact") > -1) {
    $("#contact-link").addClass("a-link-white-active");
}




if (window.location.href.indexOf("faq") > -1) {
    /* img subnav */
    $("#faq-link").addClass("a-link-white-active");
}










