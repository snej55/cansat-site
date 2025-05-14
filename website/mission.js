function mission() {
    item.innerHTML = `<h1>Our Mission</h1>
    <br><br>
    <h2>CastAway is generously supported by the Cambridge Academy for Science and Technology</h2><br> 
    <ul>
        <li>hi</li>
    <ul>
`
    document.getElementById("credits").innerHTML = "Credits";
    document.getElementById("credits").setAttribute( "onClick", "javascript: credits();" );
    document.getElementById("myDropdown").style.display = "none";
    scroll(0, 0);
}