import React, { Component } from 'react';
import { Circle, Marker } from 'react-google-maps';
import GMap from './gmap/gmap';
// import { getTransactionsAroundLocation } from './api/transactions';

class MapSection extends Component {
  state = { circleCenter: undefined };
  parentHandler = this.props.onRadiusChange;

  onClick = e => {
    const latlng = { lat: e.latLng.lat(), lng: e.latLng.lng() };
    //getTransactionsAroundLocation(latlng)
    //  .then(transactions => console.log(transactions))
    //  .then(() => {
    this.setState({ circleCenter: latlng });
    this.props.onClick(latlng);
    //  });
  };

  radiusChangedHandler = e => {
    // this.
    console.log(e);
    this.parentHandler(e);
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
        onRightClick={e => {
          this.setState({ circleCenter: undefined });
          this.props.onClick(undefined);
        }}
        onRadiusChanged={e => {
          console.log(this.props.children)
          this.radiusChangedHandler(this.radius);
        }}
      />
    );
  };

  render() {
    return (
      <GMap
        loadingElement={<div style={{ height: `100%` }} />}
        containerElement={<div style={{ height: `100%` }} />}
        mapElement={<div style={{ height: `100%` }} />}
        onClick={this.onClick}
      >
        {this.state.circleCenter !== undefined
          ? this.renderCircle(this.state.circleCenter)
          : null}
        {this.props.markers.length > 0 &&
          this.props.markers.map((marker, index) => (
            <Marker
              key={index}
              marker={marker}
              position={{ lat: marker.lat, lng: marker.lng }}
            />
          ))}
      </GMap>
    );
  }
}

export default MapSection;
