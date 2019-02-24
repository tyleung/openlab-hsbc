import React, { Component } from 'react';
import './App.css';
import Header from './header';
import InfoSection from './infoSection';
import MapSection from './mapSection';
import CategorySelectOverlay from './categorySelectOverlay';
import Footer from './footer';
import { mockSelectData } from './utils';
import { getRealtimeData, getAreaInfo } from './api/transactions';
import './api/getFirehoseAccounts';

class App extends Component {
  state = {
    selectValue: undefined,
    transactions: [],
    circleCenter: undefined,
    rtData: {},
    areaInfoData: {}
  };

  // assume point of sale
  // assume store has physical account for each location

  onMapClick = circleCenter => {
    this.setState({ circleCenter });
    getAreaInfo({ x: circleCenter.lat, y: circleCenter.lng }).then(data =>
      this.setState({ areaInfoData: data || {} })
    );
  };

  onSelectChange = e => {
    const transactions = mockSelectData[e.target.value];
    console.log(transactions);
    this.setState({ selectValue: e.target.value, transactions });
    this.beginAnimation({
      product_type: e.target.value
    });
  };

  componentDidMount() {
    this.setNewChartData();
    this.beginAnimation({
      product_type: 'Baby'
    });
  }

  setNewChartData = options => {
    return getRealtimeData({
      radius: 0.001,
      product_type: 'Baby'
    }).then(option => {
      this.setState({ rtData: option });
    });
  };

  beginAnimation = options => {
    clearInterval(this.intervalId);
    this.intervalId = setInterval(() => {
      getRealtimeData({
        radius: options.radius || 0.001,
        product_type: options.product_type
      }).then(option => this.setState({ rtData: option }));
    }, 1000);
  };

  render() {
    return (
      <div className="App">
        <div className="main-section">
          <div className="main-left">
            <Header />
            <InfoSection
              circleCenter={this.state.circleCenter}
              rtData={this.state.rtData}
              areaInfoData={this.state.areaInfoData}
            />
          </div>
          <div className="main-right">
            <CategorySelectOverlay onChange={this.onSelectChange} />
            <MapSection
              markers={this.state.transactions}
              onClick={this.onMapClick}
            />
          </div>
        </div>
        <div className="footer-section">
          <Footer />
        </div>
      </div>
    );
  }
}

export default App;
