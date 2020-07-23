$( document ).ready(function() {
    $(".organize").click(function(){
        $('.organize').css('color', '#3c78d8');
        $('.schedual').css('color', 'black');
        $('.plan').css('color', 'black');
        $('#organize').removeClass('d-none');
        $('#schedual').addClass('d-none');
        $('#plan').addClass('d-none');
    });
    $(".schedual").click(function(){
        $('.schedual').css('color', '#3c78d8');
        $('.organize').css('color', 'black');
        $('.plan').css('color', 'black');
        $('#schedual').removeClass('d-none');
        $('#organize').addClass('d-none');
        $('#plan').addClass('d-none');
    });
    $(".plan").click(function(){
        $('.plan').css('color', '#3c78d8');
        $('.schedual').css('color', 'black');
        $('.organize').css('color', 'black');
        $('#plan').removeClass('d-none');
        $('#schedual').addClass('d-none');
        $('#organize').addClass('d-none');
    });
});