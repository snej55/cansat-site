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
                            <br />
                            Some outer case prototype yap.
                        </li>
                        <br /><br />
                        <li>
                            <h4>Schematic</h4>
                            <br />
                            We have started to work on the schematic
                            <table>
                            <tr>
                                <th>parchute calculations</th>
                            </tr>
                            <tr>
                                <td>Terminal Velocity</td>
                                <td>12m/s^2</td>
                            </tr>
                            <tr>
                                <td>Total Mass</td>
                                <td>0.35kg</td>
                            </tr>
                            <tr>
                                <td>Area</td>
                                <td>0.38m^2</td>
                            </tr>
                            </table>
                        </li>
                        <br /><br />
                        <li>
                            <h4>parachute</h4>
                            <br />
                            The parachute is a very important part of the can. Without it, the can would crash to the ground 
                            and possibly leave a crater and shattered plastic. And a broken Pi Pico. That would not be good. 
                            So we have to create a parachute. The ideal descent speed is between 10 and 15 ms^-1. This is 
                            equivalent to 22 to 33 mph. The descent speed of the can and parachute is equivalent to the 
                            terminal velocity of the parachute to a first order approximation. We created a spreadsheet that 
                            calculated the ideal area of the parachute. The calculation said that the ideal area for the 
                            parachute would be 0.0225 m^2. If we create a square parachute each side lenght would be 0.15 m, 
                            or 15 cm. This is smaller than most people realise, and we did have to persuade some people that 
                            a parachute this small was the correct size. However, we can justify this size by saying that 30 
                            mph is faster than most people realise when the can is falling. If our parachute was much bigger, 
                            it would catch the wind and blow away, risking making it unrecoverable. This would void our 
                            mission, and we do not want to be disqualified for an oversized parachute.
                        </li>
                        <br /><br />
                        <li>
                            <h4>Work on the 434MHz radio (rfm69)</h4>
                            <br />
                            Some radio yap.
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    )
}