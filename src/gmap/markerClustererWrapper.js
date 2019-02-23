import React, { Component } from 'react';
import { MarkerClusterer } from 'react-google-maps/lib/components/addons/MarkerClusterer';

class MarkerClustererWrapper extends Component {
  state = {
    open: []
  };

  isOpen = id => {
    return this.state.open.includes(id);
  };

  onToggleOpen = id => {
    const open = [...this.state.open];
    var index = open.indexOf(id);
    if (index > -1) {
      open.splice(index, 1);
    } else {
      open.push(id);
    }

    this.setState({ open });
  };

  render() {
    const { MarkerComponent } = this.props;
    return (
      <MarkerClusterer
        onClick={this.props.onMarkerClustererClick}
        averageCenter
        enableRetinaIcons
        gridSize={60}
      >
        {this.props.markers.map((marker, index) => (
          <MarkerComponent
            key={index}
            marker={marker}
            isOpen={this.isOpen}
            onToggleOpen={this.onToggleOpen}
            onMarkerClick={this.props.onMarkerClick}
          />
        ))}
      </MarkerClusterer>
    );
  }
}

export default MarkerClustererWrapper;
