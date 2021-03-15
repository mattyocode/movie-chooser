var rangeSlider = function(){
    var slider = $('.range-slider'),
        range = $('.range-slider__range'),
        value = $('.range-slider__value');
      
    slider.each(function(){
  
      value.each(function(){
        var value = $(this).prev().attr('value');
        $(this).html(value);
      });
  
      range.on('input', function(){
        $(this).next(value).html(this.value);
      });
    });
  };
  
  rangeSlider();

// var addedToListToggle = function(){

//   var listBtns = document.querySelectorAll('.list-btn');
//   var cards = document.querySelectorAll('.card-body');


//   listBtns.forEach(function(btn){

//     btn.addEventListener('click', event => {
//       const cardId = e.currentTarget.parentElement.id;
//       console.log('test');
//       btn.classList.toggle('added');
//     })

//   })

// };

// addedToListToggle();