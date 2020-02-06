/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */

$(function () {
    var dropdown = $('.btn');
    var cr = $('.cr').toggle();
    var sb = $('.sb').toggle();
    var ctb = $('.ctb').toggle();

    dropdown.click(function(event) {
        cr.toggle();
        sb.toggle();
        ctb.toggle();
    })
})