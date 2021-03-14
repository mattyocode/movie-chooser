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

const addedToListToggle = function(){

  const listBtns = document.querySelectorAll('.list-btn');

  listBtns.forEach((btn) => {

    btn.addEventListener('click', function(){
      btn.classList.add('added');
    })

  })

};

addedToListToggle();