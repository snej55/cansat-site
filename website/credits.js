function credits() {

    item.innerHTML = `<h1>Credits</h1>
    <h2>cansat</h2>
`
    menuOpen = false;
    document.getElementById("credits").innerHTML = "Home";
    document.getElementById("credits").setAttribute( "onClick", "javascript: home();" );
    document.getElementById("myDropdown").style.display = "none";
}