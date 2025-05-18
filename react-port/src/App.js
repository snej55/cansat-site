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
      default:
        // return home page as default
        return Home();
    }
  }

  return (
    <div className="App">
      <div id="header">
        <img id="CastAway" src="images/logo128.png" alt="128*128 logo image" draggable="false"></img>
        <h2>CastAway</h2>

        <div id="options">
          <button id="homeButton" onClick={() => {setPage("home")}}>Home</button>
          <button id="docsButton" onClick={() => {setPage("docs")}}>Documentation</button>
          <button id="missionButton" onClick={() => {setPage("mission")}}>Mission</button>
        </div>

        <a id="menu"><i class="demo-icon icon-menu">More</i></a>
      </div>
      <div id="content">
        <p id="main-text">
          {getContent()}
        </p>
      </div>
      <footer>
        <div>
          <p>
            This Project is Open Sourced Under GNU GENERAL PUBLIC LICENSE <br></br>
            Email:&nbsp; cansat@ILoveBeans.uk.org
          </p>
          <div id="icons">
            <a id="github" href="https://github.com/snej55/cansat-site" target="_blank"><i class="demo-icon icon-github-circled-alt2 git">Github</i></a>
          </div>
        </div>
      </footer>
    </div>
  );
}

export default App;
