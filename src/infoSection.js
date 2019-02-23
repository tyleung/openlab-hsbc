import React, { Component } from 'react';
import EchartsContainer from './echartsContainer';

class InfoSection extends Component {
  render() {
    return (
      <div className="info-section">
        <span className="info-section-text">
          Click an area on the map or search by category
        </span>
        <div className="info-section-charts">
          <div className="info-section-chart-top">
            <EchartsContainer />
          </div>
          <hr />
          <div className="info-section-chart-bottom" />
        </div>
      </div>
    );
  }
}

export default InfoSection;
