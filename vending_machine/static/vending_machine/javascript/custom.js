$( document ).ready(function() {
  $("#insert-btn").click(function(event){
    event.preventDefault();
    var token = getCookie('csrftoken');
    $.post("/insert-coin",
      { csrfmiddlewaretoken: token },
      function(data){
        $("#msg").text(data.msg);
    });
  });
  $("#buy-btn").click(function(event){
    event.preventDefault();
    var token = getCookie('csrftoken');
    $.post("/buy-product",
      { csrfmiddlewaretoken: token },
      function(data){
        $("#msg").text(data.msg);
    });
  });
});

function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie != '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = jQuery.trim(cookies[i]);
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) == (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
      }
    }
  }
  return cookieValue;
}
