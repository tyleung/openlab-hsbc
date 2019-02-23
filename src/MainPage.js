import React, { Component } from 'react';
import GMap from './gmap/gmap';
import { getTransactionsAroundLocation } from './api/transactions';

class MainPage extends Component {
  onClick = e => {
    const latlng = { lat: e.latLng.lat(), lng: e.latLng.lng() };
    getTransactionsAroundLocation(latlng).then(transactions =>
      console.log(transactions)
    );
  };

  render() {
    return (
      <div>
        <GMap
          loadingElement={<div style={{ height: `100%` }} />}
          containerElement={<div style={{ height: `72vh` }} />}
          mapElement={<div style={{ height: `100%` }} />}
          onClick={this.onClick}
        />
      </div>
    );
  }
}

export default MainPage;
