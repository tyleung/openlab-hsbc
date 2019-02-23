import React from 'react';
import { withGoogleMap, GoogleMap } from 'react-google-maps';

const hongkong = { lat: 22.3964, lng: 114.1095 };

const GMap = withGoogleMap(props => (
  <GoogleMap
    id="map"
    defaultZoom={11}
    defaultCenter={hongkong}
    onClick={props.onClick}
  >
    {props.children}
  </GoogleMap>
));
export default GMap;
