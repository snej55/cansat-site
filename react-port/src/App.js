import './App.css';
import { useState } from 'react';

// different pages
import { Home } from './Components/Home';
import { Docs } from './Components/Docs';
import { Mission } from './Components/Mission';

function App() {
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

  const bgColor = {
    backgroundColor: "#0f0"
  }

  HTMLElement = {
    main: "#f0f"
  }

  return (
    <div className="App">
      <div id="header">
        <img id="CastAway" src="images/logo128.png" alt="128*128 logo" draggable="false"></img>
        <h2>CastAway</h2>

        <div id="options">
          <button className="pageButton" onClick={() => {setPage("home")}}>Home</button>
          <button className="pageButton" onClick={() => {setPage("docs")}}>Documentation</button>
          <button className="pageButton" onClick={() => {setPage("mission")}}>Mission</button>
        </div>

        <button id="menu" onclick={console.log("pressed")}><i class="demo-icon icon-menu">More</i></button>
        <div id="myDropdown" class="dropdown-content" style={bgColor}>
            <div id="theme">
                Theme &nbsp; 
                <a class="menu-item" onclick="toggleBackground(background = 0,document.cookie = 'background: 0;')"></a>
                <a class="menu-item" onclick="toggleBackground(background = 1,document.cookie = 'background: 1;')"></a>
            </div>
            <div id="PressOptions">
                <a class="menu-item" id="credits" onclick="credits()">Credits</a>
            </div>
        </div>
      </div>
      <div id="content">
        {/* <p id="main-text"> */}
          {getContent()}
        {/* </p> */}
        
      </div>
      <footer>
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
