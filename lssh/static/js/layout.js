

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

/*
if (window.location.href.indexOf("step1") > -1) {

    $( "#handin-step-1" ).removeClass( "not-selected-step" );
    $( "#handin-step-1" ).addClass( "selected-step" );

    $( "#handin-step-1-h3" ).addClass( "text-white" );

    step1 = '<h3>Information about seller</h3>'
        +'<form>'
        + '<div class="form-group">'
        + '<label for="exampleFormControlInput1">Email address</label>'
        + '<input type="email" class="form-control" id="exampleFormControlInput1" placeholder="Write email here...">'
        + '</div>'
        + '<div class="form-group">'
        + '<label for="exampleFormControlSelect1">Number of items to hand in</label>'
        + '<select class="form-control" id="exampleFormControlSelect1">'
        + '<option>1</option>'
        + '<option>2</option>'
        + '<option>3</option>'
        + '<option>4</option>'
        + '<option>5</option>'
        + '</select>'
        + '</div>'
        + '<button type="submit" onclick="toStep2()" class="btn btn-primary btn-green">Submit</button>'
        + '</form>'


      $("#hand-in-req-form").html(step1);

} */


    




/*
if (window.location.href.indexOf("step2") > -1) {

    $( "#handin-step-2" ).removeClass( "not-selected-step" );
    $( "#handin-step-2" ).addClass( "selected-step" );

    $( "#handin-step-2-h3" ).addClass( "text-white" );



    step1 = '<h3>Information about seller</h3>'
        +'<form>'
        + '<div class="form-group">'
        + '<label for="exampleFormControlInput1">Email address</label>'
        + '<input type="email" class="form-control" id="exampleFormControlInput1" placeholder="Write email here...">'
        + '</div>'
        + '<div class="form-group">'
        + '<label for="exampleFormControlSelect1">Number of items to hand in</label>'
        + '<select class="form-control" id="exampleFormControlSelect1">'
        + '<option>1</option>'
        + '<option>2</option>'
        + '<option>3</option>'
        + '<option>4</option>'
        + '<option>5</option>'
        + '</select>'
        + '</div>'
        + '<button type="submit" class="btn btn-primary btn-green">Submit</button>'
        + '</form>'
    
}*/


if (window.location.href.indexOf("contact") > -1) {
    $( "#contact-button" ).addClass( "active-help" );
    $( "#contact-button" ).removeClass( "border-help" );


    /* img subnav */
    $( "#contact-btn" ).addClass( "a-link-white-active" );
    $( "#contact-btn" ).addClass( "white-toggle " );
    $( "#contact-btn" ).removeClass( "a-link-white" );
    $( "#contact-btn" ).removeClass( "transparent-toggle" );
} 

if (window.location.href.indexOf("find_us") > -1) {
    /* img subnav */
    $( "#find-btn" ).addClass( "a-link-white-active" );
    $( "#find-btn" ).addClass( "white-toggle " );
    $( "#find-btn" ).removeClass( "a-link-white" );
    $( "#find-btn" ).removeClass( "transparent-toggle" );
} 



if (window.location.href.indexOf("faq") > -1) {

    $( "#faq-button" ).addClass( "active-help" );
    $( "#faq-button" ).removeClass( "border-help" );

    /* img subnav */
    $( "#faq-btn" ).addClass( "a-link-white-active" );
    $( "#faq-btn" ).addClass( "white-toggle " );
    $( "#faq-btn" ).removeClass( "a-link-white" );
    $( "#faq-btn" ).removeClass( "transparent-toggle" );


    title = 'GENERAL INFORMATION';
    var cardId;

    var faqCard1 = {
        cardHeader: "How does LiU Student Secondhand work?",
        cardBody: "Ipsum lorem1... ",
    };

    var faqCard2 = {
        cardHeader: "When are you open?",
        cardBody: "Ipsum lorem2... ",
    };

    var faqCard3 = {
        cardHeader: "Where are you located?",
        cardBody: "Ipsum lorem3... ",
    };

    var faqCard4 = {
        cardHeader: "Where are you located?",
        cardBody: "Ipsum lorem3... ",
    };


    

    var faqCards = [faqCard1, faqCard2, faqCard3, faqCard4];

    /*accordionTitle = '<h3 class="pb-3">' + title + '</h3>';
    $("#accordion-col").append(accordionTitle);*/

    for (cardId = 0; cardId < faqCards.length; cardId++) {

        accordionHtml = '<div id="accordion">'
        + '<div class="card">'
        + '<div class="card-header" id=' + 'heading' + cardId +
        + '</div>'
        + '<h5 class="mb-0">'
        + '<button id="faq-question-heading" class="btn btn-link" data-toggle="collapse" data-target=' + '#collapse' + cardId + ' aria-expanded="true" aria-controls=' + 'collapse' + cardId + '>'
        + '<i id="faq-angledown" class="fa fa-angle-down"></i>' + faqCards[cardId].cardHeader
        + '</button>'
        + '</h5>'
        + '</div>'      
        + '<div id=' + 'collapse' + cardId + ' class="collapse" data-parent="#accordion" aria-labelledby=' + 'heading' + cardId + '>'
        + '<div class="card-body">'
        + faqCards[cardId].cardBody
        + '</div>'
        + '</div>'
        + '</div>'
        + '</div>'
        + '</div>'
        $("#accordion-col").append(accordionHtml);
    
    }


    


}










