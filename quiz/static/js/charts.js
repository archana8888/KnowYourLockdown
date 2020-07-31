function getChartOptions(data1,data2,data3,dates,statename,name1,name2,name3) {
    var options= {
            series: [{
                name: name1,
                data: data1,
                
          },
          {
                name: name2,
                data: data2,
          },
          {
                name: name3,
                data: data3,
          }],
            colors : ['#2eba00','#ffcc02','#7f0101'],
            chart: {
                height: 350,
                type: 'area',
                foreColor: "#fff",
                zoom: {
                    enabled: false
                }   
          },
            dropShadow: {
            enabled: true,
                  opacity: 0.3,
                  blur: 5,
                  left: -7,
                  top: 22
            },
          dataLabels: {
                enabled: false
          },
          stroke: {
                curve: 'smooth'
          },
          markers:{
                size:3,
          },
          title: {
                text: statename,
                align: 'left'
          },
          tooltip :{
                theme:'dark',
          },
          grid: {
                row: {
                    colors: ['transparent','transparent'], // takes an array which will be repeated on columns  
                },
          },
          xaxis: {
                categories: dates,
                text:'Date'
          },
        };
    return options;        
};


function getBarOptions(data1,data2,data3,dates,states,name1,name2,name3){
      var options = {
            series: [{
            name: name1,
            data: data1
          }, {
            name: name2,
            data: data2
          }, {
            name: name3,
            data: data3
          }],
          colors : ['#2eba00','#ffcc02','#7f0101'],
            chart: {
            type: 'bar',
            height: 350,
            foreColor: "#fff"
          },
          plotOptions: {
            bar: {
              horizontal: false,
              columnWidth: '55%',
              endingShape: 'rounded'
            },
          },
          dataLabels: {
            enabled: false
          },
          stroke: {
            show: true,
            width: 2,
            
          },
          xaxis: {
            categories: dates,
          },
          fill: {
            opacity: 1
          },
          tooltip: {
           theme:"dark",
          },
          title: {
            text: states,
            align: 'left'
            },
      };
  return options;       
}
function getRadialOptions(data1,data2,data3,title,name1,name2,name3){
      var optionsCircle = {
            chart: {
              type: "radialBar",
              height: 350,
              offsetX: 0,
              foreColor: "#fff"
            },
            colors : ['#2eba00','#ffcc02','#7f0101'],
            plotOptions: {
              radialBar: {
                inverseOrder: false,
                hollow: {
                  margin: 5,
                  size: "48%",
                  background: "transparent"
                },
                track: {
                  show: true,
                  background: "#4F4F65",
                  strokeWidth: "100%",
                  opacity: 1,
                  margin: 3 // margin is in pixels
                }
              }
            },
            series: [data1,data2,data3],
            labels: [name1,name2,name3],
            legend: {
              show: true,
              position: "right",
              
            },
            fill: {
              type: "colors",
              gradient: {
                shade: "dark",
                type: "horizontal",
                shadeIntensity: 0.5,
                inverseColors: true,
                opacityFrom: 1,
                opacityTo: 1,
                stops: [0,100]
              }
            },
            title: {
                      text: title,
                      align: 'left'
                      },
          };
          
  
          return optionsCircle;
}
