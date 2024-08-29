$(document).ready(function () {
    var currentIndex = 0;
    var slides = $('.slides');
    var slideCount = $('.slide').length;
    var slideWidth = $('.slide').outerWidth(true);

    $('#next').click(function () {
        if (currentIndex < slideCount - 1) {
            currentIndex++;
            slides.css('transform', 'translateX(' + (-slideWidth * currentIndex) + 'px)');
        }
    });

    $('#prev').click(function () {
        if (currentIndex > 0) {
            currentIndex--;
            slides.css('transform', 'translateX(' + (-slideWidth * currentIndex) + 'px)');
        }
    });
});