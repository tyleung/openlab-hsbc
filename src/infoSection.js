import React, { Component } from 'react';
import EchartsContainer from './echartsContainer';

class InfoSection extends Component {
  render() {
    return (
      <div className="info-section">
        Click an area on the map or search for a product
        <EchartsContainer />
      </div>
    );
  }
}

export default InfoSection;
