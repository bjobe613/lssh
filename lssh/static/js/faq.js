

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
