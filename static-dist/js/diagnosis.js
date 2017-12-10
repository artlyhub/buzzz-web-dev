(function($) {
  var chart = new Highcharts.Chart({
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
          renderTo: 'container',
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
          data: [
              ['Firefox', 44.2],
              ['IE7', 26.6],
              ['IE6', 20],
              ['Chrome', 3.1],
              ['Other', 5.4]
              ]}]
    },
    // using
    function(chart) { // on complete
        var xpos = '50%';
        var ypos = '53%';
        var circleradius = 102;
    // Render the circle
    chart.renderer.circle(xpos, ypos, circleradius).attr({
        fill: '#27314f',
    }).add();
  });
})(jQuery)
