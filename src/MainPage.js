import React, { Component } from 'react';
import GMap from './gmap/gmap';

class MainPage extends Component {
  onClick = e => {
    const latlng = { lat: e.latLng.lat(), lng: e.latLng.lng() };
    console.log(latlng);
  };

  render() {
    return (
      <div>
        <GMap
          loadingElement={<div style={{ height: `100%` }} />}
          containerElement={<div style={{ height: `72vh` }} />}
          mapElement={<div style={{ height: `100%` }} />}
          onClick={this.onClick}
        />
      </div>
    );
  }
}

export default MainPage;
