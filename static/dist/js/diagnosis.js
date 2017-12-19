(function($) {

  function draw_charts() {
    var port_id = $('#saved_port_id').attr('value')

    $.ajax({
      method: "GET",
      url: '/api/portfolio/' + port_id + '/diagnosis/',
      success: function(data){
        var ratio = data.port_info.ratio
        var left_ratio = 1
        var ratio_array = []
        for (var key in ratio) {
          if (key != 'cash') {
            var ratio_point = parseFloat(ratio[key]['ratio'])
            var ratio_data = [key, ratio_point]
            ratio_array.push(ratio_data)
            left_ratio -= ratio_point
          } else {
            // pass
          }
        }
        var ratio_data = [key, left_ratio]
        ratio_array.push(ratio_data)
        console.log(ratio_array)
        draw_port_situation(ratio_array)
      },
      error: function(data){
        console.log('error')
      }
    })
  }

  draw_charts()


  function draw_port_situation(data) {
    // 포트폴리오 현황
    var port_situation_chart = new Highcharts.Chart({
        title: {
            text: '',
            style: {
                display: 'none'
            }
        },
        subtitle: {
            text: '',
            style: {
                display: 'none'
            }
        },
        chart: {
            renderTo: 'port_situation',
            type: 'pie',
            backgroundColor: '#27314f',
        },
        credits: {
            enabled: false
        },
        plotOptions: {
            pie: {
                allowPointSelect: true,
                cursor: 'pointer',
                borderColor: '#27314f',
                innerSize: '60%',
                dataLabels: {
                    enabled: true,
                    style: {
                        color: 'white'
                    }
                }
            }
        },
        series: [{
            name: '비중',
            data: data}]
      },
      // using
      function(port_situation_chart) { // on complete
          var xpos = '50%'
          var ypos = '53%'
          var circleradius = 102
      // Render the circle
      port_situation_chart.renderer.circle(xpos, ypos, circleradius).attr({
          fill: '#27314f',
      }).add()
    })
  }

  // 포트폴리오 스펙
  var port_spec_chart = new Highcharts.Chart({
    title: {
        text: ''
    },
    chart: {
        renderTo: 'port_spec',
        polar: true,
        type: 'line',
        backgroundColor: '#27314f',
    },
    credits: {
        enabled: false
    },
    pane: {
        size: '85%'
    },
    xAxis: {
        categories: ['전체', '수익성', '변동성', '안정성', '성장성', '거래량'],
        tickmarkPlacement: 'on',
        lineWidth: 0,
        labels: {
          style: {
            color: 'white'
          }
        }
    },
    yAxis: {
        gridLineInterpolation: 'polygon',
        lineWidth: 0,
        min: 0,
        max: 100,
        labels: {
          style: {
            color: 'white'
          }
        }
    },
    legend: {
        enabled: false
    },
    series: [{
        name: '점수',
        data: [90, 88, 70, 99, 86],
        pointPlacement: 'on',
        color: '#E99364'
    }]
  })

  // 사용자 포트폴리오
  var result_graph = new Highcharts.stockChart({
    title: {
        text: '',
        style: {
            display: 'none'
        }
    },
    chart: {
        renderTo: 'result_graph2',
        backgroundColor: '#27314f',
        height: 320,
    },
    credits: {
        enabled: false
    },
    xAxis: {
        tickmarkPlacement: 'on',
        lineWidth: 0,
        tickLength: 0,
        labels: {
          style: {
            color: 'silver'
          }
        }
    },
    yAxis: {
        lineWidth: 0,
        // min: 0,
        labels: {
          style: {
            color: 'white'
          }
        },
        gridLineColor: '#0A163A'
    },
    rangeSelector: {
       buttonTheme: {
          fill: '#505053',
          stroke: '#000000',
          style: {
             color: '#CCC'
          },
          states: {
             hover: {
                fill: '#707073',
                stroke: '#000000',
                style: {
                   color: 'white'
                }
             },
             select: {
                fill: '#000003',
                stroke: '#000000',
                style: {
                   color: 'white'
                }
             }
          }
       },
       inputBoxBorderColor: '#505053',
       inputStyle: {
          backgroundColor: '#333',
          color: 'silver'
       },
       labelStyle: {
          color: 'silver'
       }
    },
    navigator: {
       enabled: false
    },
    scrollbar: {
       enabled: false
    },
    series: [
    {
        name: 'Algorithm',
        data: [
          [1292198400000,59],
          [1292284800000,56.76],
          [1292371200000,45.77],
          [1292457600000,45.89],
          [1292544000000,56.80],
          [1292803200000,56.03],
          [1292889600000,58.32],
          [1292976000000,59.45],
          [1293062400000,60.23],
          [1293408000000,60.38],
          [1293494400000,60.50],
          [1293580800000,60.47],
          [1293667200000,58.24],
          [1293753600000,52.08]
        ],
        type: 'areaspline',
        threshold: null,
        tooltip: {
            valueDecimals: 2
        },
        color: 'white',
        lineWidth: 1,
        states: {
            hover: {
                enabled: true
            }
        },
        fillColor: {
            linearGradient: {
                x1: 0,
                y1: 0,
                x2: 0,
                y2: 1
            },
            stops: [
                [0, Highcharts.Color(Highcharts.getOptions().colors[7]).setOpacity(0.6).get('rgba')],
                [1, Highcharts.Color(Highcharts.getOptions().colors[0]).setOpacity(0).get('rgba')]
            ]
        }
    },
    {
        name: 'Benchmark',
        data: [
          [1292198400000,45.95],
          [1292284800000,45.76],
          [1292371200000,45.77],
          [1292457600000,45.89],
          [1292544000000,45.80],
          [1292803200000,46.03],
          [1292889600000,46.32],
          [1292976000000,46.45],
          [1293062400000,46.23],
          [1293408000000,46.38],
          [1293494400000,46.50],
          [1293580800000,46.47],
          [1293667200000,46.24],
          [1293753600000,46.08]
        ],
        tooltip: {
            valueDecimals: 2
        },
        color: 'red',
        dataLabels: {
           color: 'red'
        },
        marker: {
           lineColor: 'red'
        },
        lineWidth: 1,
        states: {
            hover: {
                enabled: true
            }
        }
    }]
  })

  // // 시장
  // var port_situation_chart = new Highcharts.Chart({
  //     title: {
  //         text: '',
  //         style: {
  //             display: 'none'
  //         }
  //     },
  //     subtitle: {
  //         text: '',
  //         style: {
  //             display: 'none'
  //         }
  //     },
  //     chart: {
  //         renderTo: 'market_chart',
  //         type: 'pie',
  //         backgroundColor: '#27314f',
  //     },
  //     credits: {
  //         enabled: false
  //     },
  //     plotOptions: {
  //         pie: {
  //             allowPointSelect: true,
  //             cursor: 'pointer',
  //             borderColor: '#27314f',
  //             innerSize: '60%',
  //             dataLabels: {
  //                 enabled: true,
  //                 style: {
  //                     color: 'white'
  //                 }
  //             }
  //         }
  //     },
  //     series: [{
  //         name: '비중',
  //         data: [
  //             ['Firefox', 44.2],
  //             ['IE7', 26.6],
  //             ['IE6', 20],
  //             ['Chrome', 3.1],
  //             ['Other', 5.4]
  //             ]}]
  //   },
  //   // using
  //   function(port_situation_chart) { // on complete
  //       var xpos = '50%'
  //       var ypos = '53%'
  //       var circleradius = 102
  //   // Render the circle
  //   port_situation_chart.renderer.circle(xpos, ypos, circleradius).attr({
  //       fill: '#27314f',
  //   }).add()
  // })
  //
  // // 사이즈
  // var port_situation_chart = new Highcharts.Chart({
  //     title: {
  //         text: '',
  //         style: {
  //             display: 'none'
  //         }
  //     },
  //     subtitle: {
  //         text: '',
  //         style: {
  //             display: 'none'
  //         }
  //     },
  //     chart: {
  //         renderTo: 'size_chart',
  //         type: 'pie',
  //         backgroundColor: '#27314f',
  //     },
  //     credits: {
  //         enabled: false
  //     },
  //     plotOptions: {
  //         pie: {
  //             allowPointSelect: true,
  //             cursor: 'pointer',
  //             borderColor: '#27314f',
  //             innerSize: '60%',
  //             dataLabels: {
  //                 enabled: true,
  //                 style: {
  //                     color: 'white'
  //                 }
  //             }
  //         }
  //     },
  //     series: [{
  //         name: '비중',
  //         data: [
  //             ['Firefox', 44.2],
  //             ['IE7', 26.6],
  //             ['IE6', 20],
  //             ['Chrome', 3.1],
  //             ['Other', 5.4]
  //             ]}]
  //   },
  //   // using
  //   function(port_situation_chart) { // on complete
  //       var xpos = '50%'
  //       var ypos = '53%'
  //       var circleradius = 102
  //   // Render the circle
  //   port_situation_chart.renderer.circle(xpos, ypos, circleradius).attr({
  //       fill: '#27314f',
  //   }).add()
  // })
  //
  // // 스타일
  // var port_situation_chart = new Highcharts.Chart({
  //     title: {
  //         text: '',
  //         style: {
  //             display: 'none'
  //         }
  //     },
  //     subtitle: {
  //         text: '',
  //         style: {
  //             display: 'none'
  //         }
  //     },
  //     chart: {
  //         renderTo: 'style_chart',
  //         type: 'pie',
  //         backgroundColor: '#27314f',
  //     },
  //     credits: {
  //         enabled: false
  //     },
  //     plotOptions: {
  //         pie: {
  //             allowPointSelect: true,
  //             cursor: 'pointer',
  //             borderColor: '#27314f',
  //             innerSize: '60%',
  //             dataLabels: {
  //                 enabled: true,
  //                 style: {
  //                     color: 'white'
  //                 }
  //             }
  //         }
  //     },
  //     series: [{
  //         name: '비중',
  //         data: [
  //             ['Firefox', 44.2],
  //             ['IE7', 26.6],
  //             ['IE6', 20],
  //             ['Chrome', 3.1],
  //             ['Other', 5.4]
  //             ]}]
  //   },
  //   // using
  //   function(port_situation_chart) { // on complete
  //       var xpos = '50%'
  //       var ypos = '53%'
  //       var circleradius = 102
  //   // Render the circle
  //   port_situation_chart.renderer.circle(xpos, ypos, circleradius).attr({
  //       fill: '#27314f',
  //   }).add()
  // })
  //
  // // 섹터
  // var port_situation_chart = new Highcharts.Chart({
  //     title: {
  //         text: '',
  //         style: {
  //             display: 'none'
  //         }
  //     },
  //     subtitle: {
  //         text: '',
  //         style: {
  //             display: 'none'
  //         }
  //     },
  //     chart: {
  //         renderTo: 'sector_chart',
  //         type: 'pie',
  //         backgroundColor: '#27314f',
  //     },
  //     credits: {
  //         enabled: false
  //     },
  //     plotOptions: {
  //         pie: {
  //             allowPointSelect: true,
  //             cursor: 'pointer',
  //             borderColor: '#27314f',
  //             innerSize: '60%',
  //             dataLabels: {
  //                 enabled: true,
  //                 style: {
  //                     color: 'white'
  //                 }
  //             }
  //         }
  //     },
  //     series: [{
  //         name: '비중',
  //         data: [
  //             ['Firefox', 44.2],
  //             ['IE7', 26.6],
  //             ['IE6', 20],
  //             ['Chrome', 3.1],
  //             ['Other', 5.4]
  //             ]}]
  //   },
  //   // using
  //   function(port_situation_chart) { // on complete
  //       var xpos = '50%'
  //       var ypos = '53%'
  //       var circleradius = 102
  //   // Render the circle
  //   port_situation_chart.renderer.circle(xpos, ypos, circleradius).attr({
  //       fill: '#27314f',
  //   }).add()
  // })

})(jQuery)
