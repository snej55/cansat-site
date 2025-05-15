function home() {

// some notes for Sebastian (self made)
// <br><br> breakspace
// <ul> bullet point list </ul>
// <li> line </li>

    item.innerHTML = `<h1>Our Mission</h1>
    <h3>We aspire to be the best we can be.</h3>
    <h3>We inspire new scientists and engineers.</h3>
    <h3>We respire to live.</h3>

    
`
if (!mobileView) {
        document.getElementById("credits").innerHTML = "Credits";
        document.getElementById("credits").setAttribute( "onClick", "javascript: credits();" );
        document.getElementById("myDropdown").style.display = "none";
        scroll(0, 0);
    }
}

home()