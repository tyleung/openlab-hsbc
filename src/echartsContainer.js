import React, { Component } from 'react';
import ReactEcharts from 'echarts-for-react';

export class EchartsContainer1 extends Component {
  render() {
    const option = {
      title: {
        text: 'chart for age distribution',
        left: 'center',
        textStyle: {
          color: '#111',
          fontStyle: 'normal',
          fontWeight: 'bold',
          fontFamily: 'sans-serif',
          fontSize: 22
        }
      },
      xAxis: {
        type: 'category',
        data: [
          '[0, 10)',
          '[21, 30)',
          '[15, 21)',
          '[10, 15)',
          '[30, 35)',
          '[35, 100)'
        ]
      },
      yAxis: {
        type: 'value'
      },
      series: [
        {
          data: [2578, 2249, 1603, 1293, 1222, 1055],
          type: 'bar'
        }
      ]
    };
    return <ReactEcharts option={option} />;
  }
}

export class EchartsContainer2 extends Component {
  render() {
    return <ReactEcharts option={this.props.option} />;
  }
}
