function docs() {
    item.innerHTML = `wats up my g bro
`
    document.getElementById("credits").innerHTML = "Credits";
    document.getElementById("credits").setAttribute( "onClick", "javascript: credits();" );
    document.getElementById("myDropdown").style.display = "none";
    scroll(0, 0);
}
