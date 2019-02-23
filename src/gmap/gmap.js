import React from 'react';
import { withGoogleMap, GoogleMap } from 'react-google-maps';

const hongkong = { lat: 22.3064, lng: 114.1795 };

const GMap = withGoogleMap(props => (
  <GoogleMap
    id="map"
    defaultZoom={12}
    defaultCenter={hongkong}
    onClick={props.onClick}
  >
    {props.children}
  </GoogleMap>
));
export default GMap;
