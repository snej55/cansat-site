function mission() {
    item.innerHTML = `<h1>Our Mission</h1>
    We aspire to develop <br> 
    <ul>
        <li>hi</li>
    <ul>
`
    document.getElementById("credits").innerHTML = "Credits";
    document.getElementById("credits").setAttribute( "onClick", "javascript: credits();" );
    document.getElementById("myDropdown").style.display = "none";
    scroll(0, 0);
}