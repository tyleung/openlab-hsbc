import React from 'react';
import { DrawingManager } from 'react-google-maps/lib/components/drawing/DrawingManager';

const DrawingManagerWrapper = props => {
  return (
    <DrawingManager
      defaultDrawingMode="circle"
      defaultOptions={{
        drawingControl: true,
        drawingControlOptions: {
          position: window.google.maps.ControlPosition.TOP_CENTER,
          drawingModes: ['circle', 'polygon', 'polyline', 'rectangle']
        },
        circleOptions: {
          fillColor: `#ffff00`,
          fillOpacity: 1,
          strokeWeight: 5,
          clickable: false,
          editable: true,
          zIndex: 1
        }
      }}
    />
  );
};

export default DrawingManagerWrapper;
