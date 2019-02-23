import React from 'react';

const Header = () => {
  return (
    <header className="header-initial App-header">
      <h1 className="header-h1 p-2">
        <span className="pr-2" />
        <img
          src={window.location.origin + '/assets/logo.png'}
          alt="logo"
          width={100}
        />
      </h1>
    </header>
  );
};

export default Header;
