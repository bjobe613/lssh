
$( "#works-buyer-button" ).click(function() {
  $("#works-seller-button").toggleClass("works-button-activated");
  $("#works-buyer-button").toggleClass("works-button-activated");
  $("#works-buyer").show();
  $("#works-seller").hide();
});

$( "#works-seller-button" ).click(function() {
  $("#works-buyer-button").toggleClass("works-button-activated");
  $("#works-seller-button").toggleClass("works-button-activated");
  $("#works-buyer").hide();
  $("#works-seller").show();
});