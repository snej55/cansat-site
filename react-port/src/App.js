import './App.css';

function App() {
  return (
    <div className="App">
      <div id="header">
        <img id="CastAway" src="images/logo128.png" alt="128*128 logo image" draggable="false"></img>
        <h2>CastAway</h2>

        <a id="menu"><i class="demo-icon icon-menu">More</i></a>
      </div>
      <div id="content">
        <p id="main-text">
          Main text
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
