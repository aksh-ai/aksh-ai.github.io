$(window).scroll(function(){
  $('nav').toggleClass('scrolled', $(this).scrollTop() > 600);
});