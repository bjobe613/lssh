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
    
            alert("Contacted us")
    
        },
        error: function (error) {
            alert("Couldn't send mail");
        }
    
      });

}