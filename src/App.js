import React, { Component } from 'react';
import './App.css';
import Header from './header';
import InfoSection from './infoSection';
import MapSection from './mapSection';
import CategorySelectOverlay from './categorySelectOverlay';
import Footer from './footer';
import { mockSelectData } from './utils';
import { getRealtimeData } from './api/transactions';
import './api/getFirehoseAccounts';

class App extends Component {
  state = {
    selectValue: undefined,
    transactions: [],
    circleCenter: undefined,
    data: {}
  };

  // assume point of sale
  // assume store has physical account for each location

  onMapClick = circleCenter => {
    this.setState({ circleCenter });
    this.beginAnimation({
      radius: 0.001,
      loc: `${Math.random()}`,
      product_type: this.state.selectValue
    })
  };

  onBubbleRadiusChange = radius => {
    console.log('new radius changed');
  }

  onSelectChange = e => {
    const transactions = mockSelectData[e.target.value];
    console.log(transactions);
    this.setState({ selectValue: e.target.value, transactions });
    this.beginAnimation({
      product_type: e.target.value
    })
  };

  componentDidMount() {
    this.setNewChartData();
    this.beginAnimation({
      product_type: 'Baby'
    });
  };

  setNewChartData = options => {
    return getRealtimeData({
      radius: 0.001,
      product_type: 'Baby',
      loc: '0'
    }).then(option => {this.setState({data: option})});
  }

  beginAnimation = options => {
    clearInterval(this.intervalId);
    this.intervalId = setInterval(() => {
      getRealtimeData({
        radius: options.radius || 0.001,
        product_type: options.product_type || 'Baby',
        loc: options.loc || '0'
      }).then(option => this.setState({ data: option }));
    }, 1000);
  }

  render() {
    return (
      <div className="App">
        <div className="main-section">
          <div className="main-left">
            <Header />
            <InfoSection circleCenter={this.state.circleCenter} data={this.state.data} />
          </div>
          <div className="main-right">
            <CategorySelectOverlay onChange={this.onSelectChange} />
            <MapSection
              markers={this.state.transactions}
              onClick={this.onMapClick}
              onRadiusChange={this.onBubbleRadiusChange}
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
