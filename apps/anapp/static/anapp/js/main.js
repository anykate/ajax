$(document).ready(function() {
  $("#contactForm").submit(function(e) {
    // prevent from normal form behaviour
    e.preventDefault();
    // serialize the form data
    var serializedData = $(this).serialize();
    $.ajax({
      type: "POST",
      url: "/ajax/contact/",
      //   url: "{% url 'anapp:contact' %}",
      data: serializedData,
      success: function(response) {
        //reset the form after successful submit
        $("#contactForm")[0].reset();
      },
      error: function(response) {
        console.log(response);
      }
    });
  });
});
