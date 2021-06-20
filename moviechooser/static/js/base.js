var rangeSlider = function () {
  var slider = $(".range-slider"),
    range = $(".range-slider__range"),
    value = $(".range-slider__value");

  slider.each(function () {
    value.each(function () {
      var value = $(this).prev().attr("value");
      $(this).html(value);
    });

    range.on("input", function () {
      $(this).next(value).html(this.value);
    });
  });
};

rangeSlider();

function toggleDetail() {
  const toggleDetailBtns = document.querySelectorAll(".toggle-detail");
  toggleDetailBtns.forEach(function (btn) {
    btn.addEventListener("click", function (e) {
      const movieCardId = e.currentTarget.dataset.id;
      const movieDetail = document.getElementById(`${movieCardId}-detail`);
      movieDetail.classList.toggle("hide");
    });
  });
}

window.addEventListener("DOMContentLoaded", function () {
  toggleDetail();
});
