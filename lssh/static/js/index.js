/********************** 
Latest items swiper
**********************/

var swiper = new Swiper('.swiper-container', {
  loop: false,
  pagination: {
    el: '.swiper-pagination',
    clickable: true,
  },
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
  breakpoints: {
    // when window width is >= 320px
    320: {
      slidesPerView: 1,
      spaceBetween: 30
    },
    // when window width is >= 480px
    480: {
      slidesPerView: 2,
      spaceBetween: 30
    },
    // when window width is >= 640px
    840: {
      slidesPerView: 3,
      spaceBetween: 30
    }
  },
});



/********************** 
Subscribe form
**********************/




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
inputSubscribe.addEventListener("keyup", function (event) {
  if (event.keyCode === 13) {
    event.preventDefault();
    email = $('#input-border-bottom').val();
    subscribeNewsLetter(email)
  }
});

/* Subscribe js */

function subscribeNewsLetter(email) {


  $.ajax({
    url: '/subscribe',
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
