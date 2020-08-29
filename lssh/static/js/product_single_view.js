
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


//Slideshow//
var swiper = new Swiper('.swiper-container', {
      slidesPerView: 1,
      spaceBetween: 30,
      loop: true,
      pagination: {
        el: '.swiper-pagination',
        clickable: true,
      },
      navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
      },
    });
