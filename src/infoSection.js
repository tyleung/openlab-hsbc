import React, { Component } from 'react';
import {
  EchartsContainerRealTime,
  EchartsContainerAreaInfo
} from './echartsContainer';

class InfoSection extends Component {
  // componentDidUpdate(prevProps) {
  //   if (prevProps.circleCenter === this.props.circleCenter) {
  //     // do nothing
  //   } else if (
  //     this.props.circleCenter !== undefined &&
  //     this.props.circleCenter !== prevProps.circleCenter
  //   ) {
  //     clearInterval(this.intervalId);
  //     this.intervalId = setInterval(() => {
  //       getRealtimeData().then(option => this.setState({ option }));
  //     }, 1000);
  //   } else {
  //     clearInterval(this.intervalId);
  //   }
  // }

  // componentWillUnmount() {
  //   clearInterval(this.intervalId);
  // }

  // componentWillUpdate() {
  //   console.log('lmfao')
  // }

  // componentDidUpdate() {
  //   console.log('lmfao')
  // }

  render() {
    return (
      <div className="info-section">
        <span className="info-section-text">
          Click an area on the map or select a category
        </span>
        <div className="info-section-charts">
          <div className="info-section-chart-top">
            <EchartsContainerRealTime option={this.props.rtData} />
          </div>
          <hr />
          {Object.keys(this.props.areaInfoData).map((objKey, index) => {
            const data = this.props.areaInfoData[objKey];
            if (data !== undefined) {
              return (
                <div key={index} className="info-section-chart-bottom">
                  <EchartsContainerAreaInfo option={data} />
                </div>
              );
            }
            return null;
          })}
        </div>
      </div>
    );
  }
}

export default InfoSection;
