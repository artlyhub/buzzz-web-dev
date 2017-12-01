( function($) {

    $(document).ready(function(){
        var origin_cotainer = $('.slider_container');
        var container = $('#slider_content');
        var count = container.children().length;
        var nav_next = $('#slider_next');
        var nav_prev = $('#slider_prev');
        var col = $('.slider_col');
        container.attr('data-all', count);

        nav_next.click(function(){
            var page_num = parseInt($('.slider_col.active').attr('data-num'))
            if (page_num == 3) {
              location.href = '/rms'
            }
            var origin_click = parseInt(origin_cotainer.attr('data-click'));
            col.removeClass('active');

            if( origin_click < count-1 ){
                origin_click++;
                origin_cotainer.attr('data-click', origin_click);
            } else {
                origin_cotainer.attr('data-click', '2');
            }
            container.css({
                'margin-left' : '-'+(origin_click*100)+'%'
            });
            $('.slider_col[data-num="'+(origin_click+1)+'"]').addClass('active');
        });

        nav_prev.click(function(){
            var page_num = parseInt($('.slider_col.active').attr('data-num'))
            if (page_num == 1) {
              location.href = '/rms'
            }
            var origin_click = parseInt(origin_cotainer.attr('data-click'));
            col.removeClass('active');

            if( origin_click > 0 ){
                origin_click--;
                origin_cotainer.attr('data-click', origin_click);
            } else {
                origin_cotainer.attr('data-click', '0');
            }
            container.css({
                'margin-left' : '-'+(origin_click*100)+'%'
            });
            $('.slider_col[data-num="'+(origin_click+1)+'"]').addClass('active');
        });
    });

})(jQuery);
