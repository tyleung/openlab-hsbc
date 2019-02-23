import React, { Component } from 'react';
import { TwitterMap } from '../gmap';
import twitterData from './data';

class TwitterPage extends Component {
  render() {
    return (
      <div>
        <TwitterMap
          twitterData={twitterData}
          userPosition={this.props.userPosition}
        />
      </div>
    );
  }
}

export default TwitterPage;
