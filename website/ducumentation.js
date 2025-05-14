function docs() {
    item.innerHTML = `<h1>Documentation</h1>
    <h2>First Prototype</h2><br>
    We started to make the prototype right away to see what we would need
`
    document.getElementById("credits").innerHTML = "Credits";
    document.getElementById("credits").setAttribute( "onClick", "javascript: credits();" );
    document.getElementById("myDropdown").style.display = "none";
    scroll(0, 0);
}
