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
                        <li>outer case prototype</li>
                        <li>Schematic</li>
                        <li>Prototype parachute</li>
                    </ul>
                </div>
            </div>
        </div>
    )
}