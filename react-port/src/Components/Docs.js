import './Docs.css';

export function Docs() {
    return (
        <div className="page-content">
            <div className="docs-text-image-block">
                <img className="docs-screenshot" src="screenshots/Screenshot 2025-05-15 at 19.37.39 - transparent.png" alt="cad model"></img>
                <div className="docs-text-block">
                    <h2>First Prototype</h2>
                    Before starting work on the actual satellite, we first worked on developing an initial prototype
                    for the satellite.
                    <br></br>
                    <h3 className="docs-subheading">What we made: </h3>
                    <ul className="docs-bullets">
                        <li><div>Outer case prototype</div></li>
                        <li><div>Schematic</div></li>
                        <li><div>Prototype parachute</div></li>
                    </ul>
                </div>
            </div>
        </div>
    )
}