import React from 'react';
import { InfoWindow, Marker } from 'react-google-maps';

const DroneMarker = ({ marker, isOpen, onToggleOpen, onMarkerClick }) => {
  return (
    <Marker
      position={{ lat: marker.lat, lng: marker.lng }}
      onClick={() => {
        onMarkerClick(marker, () => onToggleOpen(marker.id));
      }}
    >
      {isOpen(marker.id) && (
        <InfoWindow onCloseClick={() => onToggleOpen(marker.id)}>
          <span>
            <img
              src={
                window.location.origin +
                '/assets/drone-images/' +
                marker.filename
              }
              alt="drone"
              height={150}
            />
            <div className="pt-2">Distance: {marker.distance.toFixed(2)}m</div>
            <div className="pt-2">
              Latitude: {marker.lat}, Longitude: {marker.lng}
            </div>
            <div className="pt-2">{marker.content}</div>
          </span>
        </InfoWindow>
      )}
    </Marker>
  );
};

export default DroneMarker;
