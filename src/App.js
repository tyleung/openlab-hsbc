import React, { Component } from 'react';
import './App.css';
import Header from './header';
import InfoSection from './infoSection';
import MainPage from './MainPage';
import Footer from './footer';
import './api/getFirehoseAccounts';

class App extends Component {
  state = {
    showTwitter: undefined,
    userPosition: {}
  };

  onShowTwitter = val => {
    this.setState({ showTwitter: val });
  };

  // assume point of sale
  // assume store has physical account for each location

  render() {
    return (
      <div className="App">
        <div className="main-section">
          <div className="main-left">
            <Header
              showTwitter={this.state.showTwitter}
              onShowTwitter={this.onShowTwitter}
            />
            <InfoSection />
          </div>
          <div className="main-right">
            <MainPage
              showTwitter={this.state.showTwitter}
              userPosition={this.state.userPosition}
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
