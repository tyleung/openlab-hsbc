import React, { Component } from 'react';
import { GMapCustom, DroneMarker } from '../gmap';
import { distance } from '../utils';

class DroneMap extends Component {
  onMarkerClick = (marker, callback) => {
    const geocoder = new window.google.maps.Geocoder();
    const latlng = { lat: marker.lat, lng: marker.lng };
    marker.distance = distance(
      this.props.userPosition.lat,
      this.props.userPosition.lng,
      marker.lat,
      marker.lng
    );

    return geocoder.geocode({ location: latlng }, function(results, status) {
      if (status === 'OK') {
        if (results[0]) {
          marker.content = results[0].formatted_address;
        } else {
          window.alert('No results found');
        }
      } else {
        window.alert('Geocoder failed due to: ' + status);
      }

      callback();
    });
  };

  render() {
    return (
      <div className="mapContainer">
        <GMapCustom
          markers={this.props.imageData}
          MarkerComponent={DroneMarker}
          onMarkerClick={this.onMarkerClick}
          userPosition={this.props.userPosition}
        />
      </div>
    );
  }
}

export default DroneMap;
