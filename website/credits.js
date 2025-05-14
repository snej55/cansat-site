function credits() {

    item.innerHTML = `<h1>Credits</h1>
    <h2>cansat</h2>
    <br>
    <b>landing gear design:</b> <br>
    Dylan greenwood <br>
    Nathan yin <br>
 <br>
   <b> logo design and team name:</b> <br>
    Nick zyuzin <br>
    Sebastian thornton <br>
 <br>
   <b> web design:</b> <br>
    Jan Lukasiak <br>
    Jens kromdijk <br>
    Dylan greenwood <br>
    Sebastian thornton
 <br>
 
   <b> parachute design:</b> <br>
    Sebastian thornton <br>
    Dylan greenwood <br>
 <br>
   <b> prototyping:</b> <br>
    Dylan greenwood <br>
    Nathan yin <br>
 <br>
   <b> code for satelite:</b> <br>
    Nathan yin <br>
    Jens kromdijk <br>


`
    menuOpen = false;
    document.getElementById("credits").innerHTML = "Home";
    document.getElementById("credits").setAttribute( "onClick", "javascript: home();" );
    document.getElementById("myDropdown").style.display = "none";
    scroll(0, 0);
}