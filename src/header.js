import React from 'react';
import './App.css';
import { IconDrone, IconTwitter } from './icons';

const Header = props => {return (
    <header
      className={`header-initial ${
        props.showTwitter !== undefined ? 'App-header' : ''
      }`}
    >
      <h1 className="header-h1 p-2">
        <span className="pr-2">OmniAlert</span>
        <img
          src={window.location.origin + '/assets/logo.png'}
          alt="logo"
          width={60}
        />
      </h1>
      <div className="p-3">
        <button
          className={`btn ${
            props.showTwitter === true ? 'btn-primary' : 'btn-secondary'
          }`}
          active={props.showTwitter === true}
          onClick={() => props.onShowTwitter(true)}
        >
          Twitter Data <IconTwitter className="pl-1" />
        </button>{' '}
        <button
          className={`btn ${
            props.showTwitter === false ? 'btn-primary' : 'btn-secondary'
          }`}
          active={props.showTwitter === false}
          onClick={() => props.onShowTwitter(false)}
        >
          Drone Data <IconDrone className="pl-1" />
        </button>
      </div>
    </header>
  );
};

export default Header;
