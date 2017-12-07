/*
20171204 수정
*/

( function($) {
    $(document).ready(function(){
        var transCon = $('#rms_section3>.content_row_wrap');
        var transConH = transCon.outerHeight();
        var listH = $('.search_list_wrap.active').outerHeight();

        transCon.css('transform', 'translate(0, -'+(transConH-listH)/2+'px)');
    });

    $(document).on('click', '#select_submit_btn', function (){
        $('#save_submit_pop').toggleClass('active');
    });

    $(window).resize(function(){
        var transCon = $('#rms_section3>.content_row_wrap');
        var transConH = transCon.outerHeight();
        var listH = $('.search_list_wrap.active').outerHeight();

        transCon.css('transform', 'translate(0, -'+(transConH-listH)/2+'px)');
    });

    $(document).on('click', '#rms_save_list', function (){
        // $('#rms_search_list').toggleClass('active');
        $("#rms_search_list").addClass('active');
    });

    $(document).on('keydown', '#search_code', function (e){
      if (e.keyCode == 13) {
        $("#rms_search_list").addClass('active');
      }
    });

    $(document).on('click', '#search_list_submit', function (){
        $('#rms_search_list').removeClass('active');
    });

    $(document).on('click', '#search_display .display_list>a', function (){
        var list_val = $(this).text();

        $('#search_code').val(list_val);
        $("#search_display").removeClass('active');
    });

    $(document).on('keyup', '#search_code', function (){
        var codeval = $(this).val();

        if ( codeval == '' ){
            $("#search_display").removeClass('active');
        } else {
            $("#search_display").addClass('active');
        }
    });

})(jQuery);
