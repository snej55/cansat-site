function credits() {

    item.innerHTML = `<h1>Credits</h1>
    <h2>cansat</h2>
    <br>
    <b>landing gear design:</b> <br>
    Dylan greenwood <br>
    Nathan yin <br>
 <br>
   <b> logo design and team name:</b> <br>
    nick zyuzin <br>
    sebastian thorton <br>
 <br>
   <b> web design:</b> <br>
    jan Lukasiak <br>
    jens kromdijk <br>
    dylan greenwood <br>
 <br>
   <b> parachute design:</b> <br>
    sabastian thorton <br>
 <br>
   <b> prototyping:</b> <br>
    dylan greenwood <br>
    nathan yin <br>
 <br>
   <b> code for satelite:</b> <br>
    nathan yin <br>
    jens kromdijk <br>


`
    menuOpen = false;
    document.getElementById("credits").innerHTML = "Home";
    document.getElementById("credits").setAttribute( "onClick", "javascript: home();" );
    document.getElementById("myDropdown").style.display = "none";
    scroll(0, 0);
}