import React, { Component } from 'react';
import { Circle } from 'react-google-maps';
import GMap from './gmap/gmap';
import InfoSection from './infoSection';
import { getTransactionsAroundLocation } from './api/transactions';

class MainPage extends Component {
  state = { circleCenter: undefined };

  onClick = e => {
    const latlng = { lat: e.latLng.lat(), lng: e.latLng.lng() };
    //getTransactionsAroundLocation(latlng)
    //  .then(transactions => console.log(transactions))
    //  .then(() => {
    console.log(latlng);
    this.setState({ circleCenter: latlng });
    //  });
  };

  renderCircle = center => {
    return (
      <Circle
        center={center}
        radius={500}
        strokeColor="#FF0000"
        strokeOpacity={0.8}
        strokeWeight={2}
        fillColor="#FF0000"
        editable={true}
      />
    );
  };

  render() {
    return (
      <div className="main-page">
        <InfoSection />
        <div className="gmap">
          <GMap
            loadingElement={<div style={{ height: `100%` }} />}
            containerElement={<div style={{ height: `72vh` }} />}
            mapElement={<div style={{ height: `100%` }} />}
            onClick={this.onClick}
          >
            {this.state.circleCenter !== undefined
              ? this.renderCircle(this.state.circleCenter)
              : null}
          </GMap>
        </div>
      </div>
    );
  }
}

export default MainPage;
