import React, { Component } from 'react';
import { DroneMap } from '../gmap';
import imageData from './data';

class DronePage extends Component {
  render() {
    return (
      <div>
        <DroneMap
          imageData={imageData}
          userPosition={this.props.userPosition}
        />
      </div>
    );
  }
}

export default DronePage;
