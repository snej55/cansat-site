function home() {

// some notes for Sebastian (self made)
// <br><br> breakspace
// <ul> bullet point list </ul>
// <li> line </li>

    item.innerHTML = `<h1>Home</h1>
    <img src="public/images/logo.png">
    We are a team of young engineers 

    
`
    if (!mobileView) {
        document.getElementById("credits").innerHTML = "Credits";
        document.getElementById("credits").setAttribute( "onClick", "javascript: credits();" );
    }
    menuOpen = false;
    document.getElementById("myDropdown").style.display = "none";
    scroll(0, 0);
    credit = false
    close()
}

home()