function credits() {

    item.innerHTML = `<h1>Credits</h1>
    <h2>cansat</h2>
    landing gear design: <br>
    Dylan greenwood <br>
    Nathan yin <br>
 <br>
    logo design: <br>
    nick zyuzin <br>
 <br>
    web design: <br>
    jan Lukasiak <br>
    jens kromdijk <br>
    dylan greenwood <br>
 <br>
    parachute design: <br>
    sabastian thorton <br>
 <br>
    prototyping: <br>
    dylan greenwood <br>
    nathan yin <br>
 <br>
    code for satelite: <br>
    nathan yin <br>
    jens kromdijk <br>


`
    menuOpen = false;
    document.getElementById("credits").innerHTML = "Home";
    document.getElementById("credits").setAttribute( "onClick", "javascript: home();" );
    document.getElementById("myDropdown").style.display = "none";
    scroll(0, 0);
}