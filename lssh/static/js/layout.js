
//Scroll navbar
$(document).scroll(function () {
    var $nav = $("#navbar");
    $nav.toggleClass('scrolled', $(this).scrollTop() > 0);
});

if (window.history.replaceState) {
    window.history.replaceState(null, null, window.location.href);
}

if (window.location.href.indexOf("about") > -1) {
    $("#navbar").removeClass("fixed-top");
}

if (window.location.href.indexOf("help") > -1) {
    $("#navbar").removeClass("fixed-top");

}

if (window.location.href.indexOf("hand_in") > -1) {
    $("#navbar").removeClass("fixed-top");
}

if (window.location.href.indexOf("products") > -1) {
    $("#navbar").removeClass("fixed-top");
}

if (window.location.href.indexOf("contact") > -1) {
    /* img subnav */
    $("#contact-btn").addClass("a-link-white-active");
    $("#contact-btn").addClass("white-toggle ");
    $("#contact-btn").removeClass("a-link-white");
    $("#contact-btn").removeClass("transparent-toggle");
}

if (window.location.href.indexOf("find_us") > -1) {
    /* img subnav */
    $("#find-btn").addClass("a-link-white-active");
    $("#find-btn").addClass("white-toggle ");
    $("#find-btn").removeClass("a-link-white");
    $("#find-btn").removeClass("transparent-toggle");
}

if (window.location.href.indexOf("faq") > -1) {
    /* img subnav */
    $("#faq-btn").addClass("a-link-white-active");
    $("#faq-btn").addClass("white-toggle ");
    $("#faq-btn").removeClass("a-link-white");
    $("#faq-btn").removeClass("transparent-toggle");
}










