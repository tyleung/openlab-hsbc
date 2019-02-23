import React, { Component } from 'react';
import TwitterPage from './twitter';
import DronePage from './drone';

class MainPage extends Component {
  render() {
    return (
      <div
        className={
          this.props.showTwitter !== undefined
            ? 'mainContainer'
            : 'mainContainer-collapsed'
        }
      >
        {this.props.showTwitter === true && (
          <TwitterPage userPosition={this.props.userPosition} />
        )}
        {this.props.showTwitter === false && (
          <DronePage userPosition={this.props.userPosition} />
        )}
      </div>
    );
  }
}

export default MainPage;
