function docs() {
    item.innerHTML = `<h1>Documentation </h1> <br>
    <h2>First Prototype </h2> 
    We started to make the prototype right away to see what we would need for the design and construction of the satelite. <br>
    we done this to leve as much of our budget for the final build and not all for the protottype to give us the best <br>
    satelite we can get out of the budget we have. <br><br>
    <h3>What we made </h3>
    <ul>
        <li>outer case prototype </li>
        <li>schematic </li>
        <li>prototype parachute </li>
    </ul> <br>
    <img src="../src/assets/Screenshot 2025-05-15 at 19.37.39 - transparent.png">
    hello

`
    if (!mobileView) {
        document.getElementById("credits").innerHTML = "Credits";
        document.getElementById("credits").setAttribute( "onClick", "javascript: credits();" );
    }
    menuOpen = false;
    document.getElementById("myDropdown").style.display = "none";
    credit = false
    scroll(0, 0);
    close()
}