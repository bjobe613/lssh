var serverUrl = 'http://localhost:5000'


$("#works-buyer-button").click(function () {
  $("#works-seller-button").toggleClass("works-button-activated");
  $("#works-buyer-button").toggleClass("works-button-activated");
  $("#works-buyer").show();
  $("#works-seller").hide();
});

$("#works-seller-button").click(function () {
  $("#works-buyer-button").toggleClass("works-button-activated");
  $("#works-seller-button").toggleClass("works-button-activated");
  $("#works-buyer").hide();
  $("#works-seller").show();
});

function subscribeButton() {
  
  email = $('#input-border-bottom').val();
  subscribeNewsLetter(email);
} 




// Event listener on enter button for input for subscribe
var inputSubscribe = document.getElementById("input-border-bottom");
  inputSubscribe.addEventListener("keyup", function(event) {
    if (event.keyCode === 13) {
      event.preventDefault();
      email = $('#input-border-bottom').val();
      subscribeNewsLetter(email)
  }
});

/* Subscribe js */

function subscribeNewsLetter(email) {


  $.ajax({
    url: serverUrl + '/subscribe',
    type: 'POST',
    contentType: "application/json",
    data: JSON.stringify(email),
    success: function (res) { 

      subscribeSuccess = '<div class="col text-center pb-3">'
      + '<h3> SUBSCRIBED! </h3>'
      + '<p>Thank you for subscribing to our newsletter.</p>'
      + '</div>'

      $("#subscribe-space").html(subscribeSuccess);
      $("#subscribe-row").hide();

    },
    error: function (error) {
        alert("Already subscribed or undefined email");
    }

  });
}
