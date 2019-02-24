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
  };

  onSelectChange = e => {
    const transactions = mockSelectData[e.target.value];
    console.log(transactions);
    this.setState({ selectValue: e.target.value, transactions });
  };

  componentDidMount() {
    this.setNewChartData();
    this.beginAnimation();
  };

  setNewChartData = options => {
    return getRealtimeData({
      radius: 12,
      product_type: 'asdf'
    }).then(option => {this.setState({data: option})});
  }

  beginAnimation = options => {
    clearInterval(this.intervalId);
    this.intervalId = setInterval(() => {
      getRealtimeData({
        radius: 12,
        product_type: 'asdf'
      }).then(option => this.setState({ option }));
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
