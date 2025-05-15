function credits() {

    item.innerHTML = `<h1>Credits</h1>

    <h2>landing gear design:</h2>
    Dylan greenwood <br>
    Nathan yin <br><br>

   <h2> logo design and team name:</h2>
    Nick zyuzin <br>
    Sebastian thornton <br><br>

   <h2> web design:</h2>
    Jan Lukasiak <br>
    Jens kromdijk <br>
    Dylan greenwood <br>
    Sebastian thornton <br><br>

   <h2> parachute design:</h2>
    Sebastian thornton <br>
    Dylan greenwood <br><br>

   <h2> prototyping:</h2>
    Dylan greenwood <br>
    Nathan yin <br><br>

   <h2> code for satelite:</h2>
    Nathan yin <br>
    Jens kromdijk <br>


`
    menuOpen = false;
    document.getElementById("credits").innerHTML = "Home";
    document.getElementById("credits").setAttribute( "onClick", "javascript: home();" );
    document.getElementById("myDropdown").style.display = "none";
    scroll(0, 0);
}