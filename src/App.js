import React, { Component } from 'react';
import './App.css';
import Header from './header';
import InfoSection from './infoSection';
import MapSection from './mapSection';
import CategorySelectOverlay from './categorySelectOverlay';
import Footer from './footer';
import { mockSelectData } from './utils';
import './api/getFirehoseAccounts';

class App extends Component {
  state = {
    selectValue: undefined,
    transactions: [],
    circleCenter: undefined
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

  render() {
    return (
      <div className="App">
        <div className="main-section">
          <div className="main-left">
            <Header />
            <InfoSection circleCenter={this.state.circleCenter} />
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
