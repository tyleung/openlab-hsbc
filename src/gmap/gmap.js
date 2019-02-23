import React from 'react';
import { withGoogleMap, GoogleMap } from 'react-google-maps';

const china = { lat: 39.913818, lng: 116.363625 };

const GMap = withGoogleMap(props => {
  return (
    <GoogleMap
      id="map"
      defaultZoom={4}
      defaultCenter={china}
      ref={map => {
        if (map && props.shouldFitBounds) {
          map.fitBounds(props.bounds);
          props.toggleFitBounds();
        }
      }}
    >
      {props.children}
    </GoogleMap>
  );
});

export default GMap;
