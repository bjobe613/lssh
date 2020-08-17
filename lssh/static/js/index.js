
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



$("#input-border-button").click(function () {

  email = $('#input-border-bottom').val();
  alert(email);

  subscribeNewsLetter(email)
});

/* Subscribe js */

function subscribeNewsLetter(email) {
  $.ajax({
    url: '/',
    type: 'POST',
    contentType: "application/json",
    data: JSON.stringify(email),
    success: function (res) { 
      alert("success email sent to db!") 
    }
  });
}