ScrollReveal().reveal('.text2', { 
  duration: 1600, 
  scale: 4,
  reset: true
});

ScrollReveal().reveal('.text3', { 
  duration: 1600, 
  origin: 'left', 
  distance: '50px',
  reset: true   
});

ScrollReveal().reveal('.text4', { 
  duration: 1600, 
  origin: 'right', 
  distance: '50px',
  reset: true   
});

ScrollReveal().reveal('.text5', { 
  duration: 1600, 
  origin: 'top', 
  distance: '50px',
  reset: true   
});

ScrollReveal().reveal('.text6', { 
  duration: 1600, 
  scale: 0.1,
  reset: true
});

ScrollReveal().reveal('.image1', { 
  duration: 1600,
  reset: true   
});



ScrollReveal().reveal('.slide-bottom', { 
  duration: 1600, 
  origin: 'bottom', 
  distance: '100px',
  reset: true,   
  mobile: true
});


ScrollReveal().reveal('.first', { 
  duration: 1600, 
  origin: 'left', 
  distance: '100px',
  reset: true,   
  mobile: true
});

ScrollReveal().reveal('.second', { 
  duration: 1600, 
  origin: 'right', 
  distance: '100px',
  reset: true,   
  mobile: true
});

ScrollReveal().reveal('#blog', { 
  duration: 3000,
  reset: true   
});


// $(function(){
//   $(`#blind_menu`).hide();
//   $('.menu-trigger.active').hide();
//   $('#hamburger').click(function(e){
//     $('#blind_menu').show();
//     $('.menu-trigger').hide();
//     $('.menu-trigger.active').show();
//     $('#hamburger').click(function(e){
//       $('#blind_menu').hide();
//       $('.menu-trigger').show();
//       $('.menu-trigger.active').hide();
//     })
//   })
// })


$(function(){
  $('#hamburger').click(function(e){
    $('.menu-trigger').toggleClass('active');
    $('#blind_menu').toggleClass('open_menu');
  });
});