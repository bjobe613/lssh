function contactForm() {
    alert("contact");

    $.ajax({
        url: '/contact/form',
        type: 'POST',
        contentType: "application/json",
        data: JSON.stringify(email),
        success: function (res) { 
    
            alert("Contacted us")
    
        },
        error: function (error) {
            alert("Couldn't send mail");
        }
    
      });

}