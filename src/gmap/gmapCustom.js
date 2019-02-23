import React, { Component } from 'react';
import GMap from './gmap';
import MarkerClustererWrapper from './markerClustererWrapper';

class GMapCustom extends Component {
  API_KEY = 'AIzaSyCVXxT3CCxfcNO5yKJpa62CO9mGCJX5CV8';

  state = {
    bounds: {},
    shouldFitBounds: true
  };

  componentDidMount() {
    const bounds = new window.google.maps.LatLngBounds();
    this.props.markers.map((marker, i) => {
      return bounds.extend(
        new window.google.maps.LatLng(marker.lat, marker.lng)
      );
    });

    this.setState({ bounds });
  }

  toggleFitBounds = () => {
    this.setState({ shouldFitBounds: false });
  };

  render() {
    return (
      <GMap
        googleMapURL={`https://maps.googleapis.com/maps/api/js?key=${
          this.API_KEY
        }&v=3.exp&libraries=geometry,drawing,places`}
        loadingElement={<div style={{ height: `100%` }} />}
        containerElement={<div style={{ height: `72vh` }} />}
        mapElement={<div style={{ height: `100%` }} />}
        bounds={this.state.bounds}
        shouldFitBounds={this.state.shouldFitBounds}
        toggleFitBounds={this.toggleFitBounds}
      >
        <MarkerClustererWrapper
          markers={this.props.markers}
          onMarkerClustererClick={this.props.onMarkerClustererClick}
          onMarkerClick={this.props.onMarkerClick}
          MarkerComponent={this.props.MarkerComponent}
          userPosition={this.props.userPosition}
        />
        {/*
        {Object.keys(this.props.userPosition).length !== 0 && (
          <Marker
            icon={window.location.origin + '/assets/icons/walking.svg'}
            position={this.props.userPosition}
          />
        )}
        */}
      </GMap>
    );
  }
}

export default GMapCustom;
