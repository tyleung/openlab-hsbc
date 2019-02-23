import React, { Component } from 'react';
import './App.css';
import Header from './header';
import MainPage from './MainPage';
import Footer from './footer';

class App extends Component {
  state = {
    showTwitter: undefined,
    userPosition: {}
  };

  onShowTwitter = val => {
    this.setState({ showTwitter: val });
  };

  render() {
    return (
      <div className="App">
        <Header
          showTwitter={this.state.showTwitter}
          onShowTwitter={this.onShowTwitter}
        />
        <MainPage
          showTwitter={this.state.showTwitter}
          userPosition={this.state.userPosition}
        />
        <Footer />
      </div>
    );
  }
}

export default App;
