( function($) {

    function save_portfolio_data() {
      var capital = parseInt($('#capital_set').val())
      $.ajax({
        method: "POST",
        url: '/api/portfolio/',
        data: {
            'capital': capital,
        },
        success: function(data){
          $('#capital_amt').text(String(data.capital) + '원')
        },
        error: function(data){
          console.log('error')
          console.log(data)
        }
      })
    }

    $(document).on('click', '#save_capital_btn', function () {
      var capital_amt = $('#capital_set').val()
      if (!capital_amt | 0 === capital_amt.length) {
        $('#capital_amt').text('10,000,000원')
        $('#slider_next').click()
      } else {
        $('#capital_amt').text(String(capital_amt) + '원')
        $('#slider_next').click()
      }
    })

    $(document).on('keydown', '#capital_set', function (e) {
      if (e.keyCode == 13) {
        var capital_amt = $('#capital_set').val()
        if (!capital_amt | 0 === capital_amt.length) {
          $('#capital_amt').text('0')
          $('#slider_next').click()
        } else {
          $('#capital_amt').text(String(capital_amt) + '원')
          $('#slider_next').click()
        }
      }
    })

    $(document).on('click', '#stock_btn', function () {
      $('#kinds_type').text('주식형')
      $('#slider_next').click()
    })

    $(document).on('click', '#stock_cash_btn', function () {
      $('#kinds_type').text('현금 + 주식형')
      $('#slider_next').click()
    })

    Number.prototype.pad = function(size) {
      var s = String(this);
      while (s.length < (size || 2)) {s = "0" + s;}
      return s;
    }

    String.prototype.format = function() {
      var formatted = this
      for (var i = 0; i < arguments.length; i++) {
          var regexp = new RegExp('\\{'+i+'\\}', 'gi')
          formatted = formatted.replace(regexp, arguments[i])
      }
      return formatted
    }

    function check_recent_ticker_update(ticker) {
      $.ajax({
        method: "GET",
        url: '/api/ticker-updated',
        success: function(data){
          check_ticker_exists(data.updated_date, ticker)
        },
        error: function(data){
          console.log('error')
          console.log(data)
        }
      })
    }

    function check_ticker_exists(date, ticker) {
      $.ajax({
        method: "GET",
        url: '/api/ticker/?date=' + date + '&code=' + ticker,
        success: function(data){
          var name = data.results[0].name
          var ticker = data.results[0].code
          add_code_list(name, ticker)
        },
        error: function(data){
          console.log('error')
          console.log(data)
        }
      })
    }

    function add_code_list(name, ticker) {
      var code_list = `
      <div class="list_col">
          <div class="list_col_title">{0} {1}</div>
          <a class="list_del_btn">삭제</a>
      </div>
      `.format(name, ticker)
      $('.search_list').append(code_list)
      codes_list.push(ticker)
    }

    var codes_list = []
    $(document).on('click', '#rms_save_list', function () {
      var search_code = $('#search_code').val()
      if (search_code != '') {
        check_recent_ticker_update(search_code)
      } else if (search_code == '') {
        // pass
      }
    })

    $(document).on('keydown', '#search_code', function () {
        if (e.keyCode == 13) {
          var search_code = $('#search_code').val()
          if (search_code != '') {
            check_recent_ticker_update(search_code)
          } else if (search_code == '') {
            // pass
          }
        }
    })

    $(document).on('click', '.list_del_btn', function () {
      var list_col = $(this).parents('.list_col').text()
      var list_col_text = list_col.replace(/\s+/g, '')
      var string_length = list_col_text.length
      var ticker = list_col_text.substr(string_length-8, 6)
      codes_list = codes_list.filter(function(code) {
        return code != ticker
      })
      $(this).parents('.list_col').remove()
    })

})(jQuery);
