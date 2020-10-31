function contactForm() {
  

 
    data = {
        "name": $("#input-contact-name").val(),
        "email": $("#input-contact-email").val(),
        "message": $("#input-contact-message").val()
    }

    $.ajax({
        url: '/contactform',
        type: 'POST',
        contentType: "application/json",
        data: JSON.stringify(data),
        success: function (res) { 

            contactSuccess = '<div class="col text-center pb-3">'
            + '<h3> Thank you for your message! </h3>'
            + '<p>We will be in touch with you soon</p>'
            + '</div>'
      
            $("#contact-success").html(contactSuccess);
            $("#contact-col").hide();
    
        },
        error: function (error) {
      
        }
    
      });

}