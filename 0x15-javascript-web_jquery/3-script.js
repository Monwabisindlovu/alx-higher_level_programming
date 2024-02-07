/*
   This script adds functionality to the HTML document by using jQuery.
   It targets the element with the id "red_header" and adds an event listener
   to it. When this element is clicked, it applies the class "red" to the
   <header> element, effectively changing its text color to red.
*/
$(document).ready(function() {
  $('#red_header').click(function() {
    $('header').addClass('red');
  });
});

