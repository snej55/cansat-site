import './Docs.css';

export function Docs() {
    return (
        <div>
            <div id="allign">
                <div id="left">
                    <img className="docs-screenshot" src="screenshots/Screenshot 2025-05-15 at 19.37.39 - transparent.png" alt="cad model"></img>
                </div>
                <div id="right">
                    <h2>First Prototype</h2>
                    <p>
                        Before starting work on the actual satellite, we first worked on developing an initial prototype
                        for the satellite.
                    </p>
                    <br />
                    <h3 className="docs-subheading">What we made: </h3>
                    <ul className="docs-bullets">
                        <li>
                            <h4>outer case prototype</h4>
                        </li>
                        <li>
                            <h4>Schematic</h4>
                            We have started to work on the schematic
                        </li>
                        <li>
                            <h4>parachute</h4>
                            parachute is crazy
                        </li>
                        <li>
                            <h4>Work on the 434MHz radio (rfm69)</h4>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    )
}