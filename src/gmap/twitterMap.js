import React, { Component } from 'react';
import { GMapCustom, TwitterMarker } from '.';

class TwitterMap extends Component {
  onMarkerClick = (marker, callback) => {
    const geocoder = new window.google.maps.Geocoder();
    const latlng = { lat: marker.lat, lng: marker.lng };
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
          markers={this.props.twitterData}
          MarkerComponent={TwitterMarker}
          onMarkerClick={this.onMarkerClick}
          userPosition={this.props.userPosition}
        />
      </div>
    );
  }
}

export default TwitterMap;
