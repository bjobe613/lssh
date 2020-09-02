$('document').ready(function(){
  var current_url = window.location.href;
  $(".fb-share-button").attr("data-href", current_url);
});
