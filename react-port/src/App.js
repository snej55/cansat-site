import './App.css';
import { useState } from 'react';

// different pages
import { Home } from './Components/Home';
import { Docs } from './Components/Docs';
import { Mission } from './Components/Mission';

import { darkModeInnit } from './cookies';

function App() {

  const [darkMode, toogleDarkMode] = useState(darkModeInnit);

  let root = {
    red: "#b13e53",
    orange: "#ef7d57",
    yellow: "#ffcd75",
    lime: "#a7f070",
    green: "#28a754",
    blue: "#257179",
    white: "#f4f4f6",
    lightGrey: "#adb0b5",
    grey: "#696c70",
    darkGrey: "#33373a",
    black: "#1a1a1d",
  }

  let accentColor = darkMode ? root.blue : root.darkGrey
  let bgColor = darkMode ? root.black : root.white
  let textColor = darkMode ? "#fff" : "#000"

  const [page, setPage] = useState('home');

  function getContent() {
    switch (page) {
      case "home":
        return Home();
      case "docs":
        return Docs();
      case "mission":
        return Mission();
      case "credits":
        return "";
      default:
        // return home page as default
        return Home();
    }
  }

  return (
    <div id="App" style={{backgroundColor: bgColor}}>
      <div id="header" style={{backgroundColor: accentColor}}>
        <img id="CastAway" src="images/logo128.png" alt="128*128 logo" draggable="false"></img>
        <h2>CastAway</h2>

        <div id="options">
          <button className="pageButton" onClick={() => {setPage("home")}}>Home</button>
          <button className="pageButton" onClick={() => {setPage("docs")}}>Documentation</button>
          <button className="pageButton" onClick={() => {setPage("mission")}}>Mission</button>
        </div>

        <button id="menu"><i className="demo-icon icon-menu">More</i></button>
        <div id="myDropdown" className="dropdown-content">
            <div id="theme">
                Theme &nbsp; 
                <a class="menu-item"></a>
                <a class="menu-item"></a>
            </div>
            <div id="PressOptions">
                <a className="menu-item" id="credits" onclick="credits()">Credits</a>
            </div>
            <button onClick={() => {toogleDarkMode(0); document.cookie = "background: 0"}}>white</button>
            <button onClick={() => {toogleDarkMode(1); document.cookie = "background: 1"}}>dark</button>
        </div>
      </div>
      <div id="content" style={{backgroundColor: bgColor, color: textColor}}> {/* else {return("#000")}})}>*/}
        {/* <p id="main-text"> */}
          {getContent()}
        {/* </p> */}
        testing
      </div>
      <footer style={{backgroundColor: accentColor}}>
        <div>
          <p>
            This Project is Open Sourced Under GNU GENERAL PUBLIC LICENSE <br></br>
            Email:&nbsp; cansat@ILoveBeans.uk.org
          </p>
          <div id="icons">
            <a id="github" href="https://github.com/snej55/cansat-site" target="_blank" rel="noreferrer"><i class="demo-icon icon-github-circled-alt2 git"></i></a>
          </div>
        </div>
      </footer>
    </div>
  );
}

export default App;
