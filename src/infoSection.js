import React, { Component } from 'react';
import { EchartsContainer2 } from './echartsContainer';
import { getRealtimeData } from './api/transactions';

class InfoSection extends Component {
  state = {
    option: {}
  };

  componentDidUpdate(prevProps) {
    if (prevProps.circleCenter === this.props.circleCenter) {
      // do nothing
    } else if (
      this.props.circleCenter !== undefined &&
      this.props.circleCenter !== prevProps.circleCenter
    ) {
      clearInterval(this.intervalId);
      this.intervalId = setInterval(() => {
        getRealtimeData().then(option => this.setState({ option }));
      }, 1000);
    } else {
      clearInterval(this.intervalId);
    }
  }

  componentWillUnmount() {
    clearInterval(this.intervalId);
  }

  render() {
    return (
      <div className="info-section">
        <span className="info-section-text">
          Click an area on the map or select a category
        </span>
        <div className="info-section-charts">
          <div className="info-section-chart-top" />
          <hr />
          <div className="info-section-chart-bottom">
            <EchartsContainer2 option={this.state.option} />
          </div>
        </div>
      </div>
    );
  }
}

export default InfoSection;
