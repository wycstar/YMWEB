$(document).ready(function(){
    $(".top-nav-item a").click(function(){
        $(".top-nav-item-a-active").removeClass('top-nav-item-a-active');
        $(this).addClass('top-nav-item-a-active')
    });
    //$("#s").click(function(event) {
    //    $(this).addClass('form-input-active')
    //});
    //$(document).click(function(event) {
    //    if(!$(event.target).is("#main-input")){
    //        alert('aaa')
    //    }
    //});
    $(":text").focus(function(event) {
        $("#main-input").addClass('form-input-active')
    });
    $(":text").blur(function(event) {
        $("#main-input").removeClass('form-input-active')
    });
});