import React from 'react';
import { InfoWindow, Marker } from 'react-google-maps';

const TwitterMarker = ({ marker, isOpen, onToggleOpen, onMarkerClick }) => {
  return (
    <Marker
      position={{ lat: marker.lat, lng: marker.lng }}
      onClick={() => {
        onMarkerClick(marker, () => onToggleOpen(marker.id));
      }}
    >
      {isOpen(marker.id) && (
        <InfoWindow onCloseClick={() => onToggleOpen(marker.id)} />
      )}
    </Marker>
  );
};

export default TwitterMarker;
