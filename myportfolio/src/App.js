import logo from './logo.svg';
import './App.css';
import React, { useState, useEffect } from 'react';

function App() {
  const [currentTime, setCurrentTime] =  useState(0);

  useEffect(()=>{
    fetch('/time').then(res => res.json()).then(data => {
      setCurrentTime(data.time)
      })

    }, [])

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <a
          className="App-link"
          href=""
          target="_blank"
          rel="noopener noreferrer"
        >
          The current time is {currentTime}.
        </a>
      </header>
    </div>
  );
}

export default App;
