$(document).ready(function(){
    $('.key-submit').mouseover(function(event) {
        $(this).addClass('key-submit-hover');
    });
    $('.key-submit').mouseleave(function(event) {
        $(this).removeClass('key-submit-hover');
    });
    $('#pager-nav-left').mouseover(function(event) {
        $(this).addClass('pager-nav-left-hover');
    });
    $('#pager-nav-left').mouseleave(function(event) {
        $(this).removeClass('pager-nav-left-hover');
    });
    $('#pager-nav-right').mouseover(function(event) {
        $(this).addClass('pager-nav-right-hover');
    });
    $('#pager-nav-right').mouseleave(function(event) {
        $(this).removeClass('pager-nav-right-hover');
    });
    $(document).scroll(function(event) {
        if(($(document.body).scrollTop() + $(document.documentElement).scrollTop()) > 70){
            $('#zhihu-zone').removeClass('result-extra');
            $('#zhihu-zone').addClass('result-extra-fixed');
        }
        else if($(document.body).scrollTop() <=70){
            $('#zhihu-zone').removeClass('result-extra-fixed');
            $('#zhihu-zone').addClass('result-extra');
        }
    });
});