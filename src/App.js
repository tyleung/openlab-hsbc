import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import { getCurrentUser } from './api';

class App extends Component {
  btnTest = () => {
    getCurrentUser().then(currUser => console.log(currUser));
  };

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            Edit <code>src/App.js</code> and save to reload.
          </p>
          <a
            className="App-link"
            href="https://reactjs.org"
            target="_blank"
            rel="noopener noreferrer"
          >
            Learn React
          </a>
          <button className="primary" onClick={this.btnTest}>
            Get current user
          </button>
        </header>
      </div>
    );
  }
}

export default App;