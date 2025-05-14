function credits() {

    item.innerHTML = `<h1>Credits</h1>
    <h2>cansat</h2>
    landing gear design:
    Dylan greenwood
    Nathan yin

    logo design:
    nick zyuzin

    web design:
    jan Lukasiak
    jens kromdijk
    dylan greenwood

    parachute design:
    sabastian thorton

    prototyping:
    dylan greenwood
    nathan yin

    code for satelite:
    nathan yin
    jens kromdijk


`
    menuOpen = false;
    document.getElementById("credits").innerHTML = "Home";
    document.getElementById("credits").setAttribute( "onClick", "javascript: home();" );
    document.getElementById("myDropdown").style.display = "none";
    scroll(0, 0);
}